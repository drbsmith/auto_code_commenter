"""! @file

# Header Generator

Checks for the presence of a header block (this comment block), and either fills it in, or replaces it if forced.

## Classes
	* headerClass

## Functions
	* CheckForHeader
	* RemoveHeader
	* FilenameToTitle
	* PackageFromFilename
	* RollupFunctions
	* RollupClasses
	* MakeHeader
	* BuildHeader
@package src"""

## If True inject a rollup of Class definitions in the header block
INCLUDE_CLASSES = True

## If True inject a rollup of Function definitions in the header block
INCLUDE_FUNCTIONS = True

## Template used to generate the header block.
# TODO: move to a file that can be specified without modifying this code.
HEADER_TEMPLATE = '''"""! @file

# {}

TODO_DOC

[CLASSES]
[FUNCTIONS]
[POST]
@package {}"""

'''

## Rename original: keeps the original source file with a new suffix
RENAME_ORIGINAL = True

import sys, os

from util.log import setup_logging
logger = setup_logging('header_generator.py')


def CheckForHeader(lines):
	"""! the header should be the first thing in the file
	Look for a complete comment block
	"""

	# perform initial cleanup, remove empty lines
	code = [l for l in lines if l != '']

	header = None
	exists = False
	for x in code:
		if exists:
			header += x + '\n'
			if x.find('"""') > -1: # end of header
				break
		# do this test second to not trigger end test
		if x[:4] == '"""!':
			# fully left justified comment block. Should be the file header, but could it be somewhere else in the file?
			# Todo: confirm it's the header. Is it worse to return nothing or inject a duplicate header?
			exists = True
			header = x + '\n'

	return header

def RemoveHeader(code):
	s = code.find('"""!')

	e = code[s+4:].find('"""') + (s+4) + 3

	ret = code[:s] + code[e:]

	return ret

def FilenameToTitle(fname):
	"""! try to convert a filename to a title """

	# take off filename itself, drop extension
	if fname.find('/') != -1:
		x = len(fname) - fname[::-1].find('/')

		fname = fname[x:]

	if fname.find('.') != -1:
		fname = fname[: fname.find('.')]

	# what case is it in? Convert anything to snake, then split to a title

	# test for all upper:
	if fname.upper() == fname:
		fname = fname.lower()

	if fname.lower() != fname: # camel
		x = ''
		for f in fname:
			if f.lower() != f:
				x += '_'
				x += f.lower()
			else: x += f

		fname = x

	while fname[0] == '_': # drop leading underscores. Above loop injects one if file has initial caps
		fname = fname[1:]

	title = fname.replace('_', ' ').title()

	return title # that was fun, let's go!

def PackageFromFilename(fname: str) -> str:
	"""!
	If filename has a folder use that as the package designation.

	@param fname (str): name of file (with path) to extract the package name (enclosing folder).
	@return (str) the extracted package name, if found in supplied path (fname).
	"""

	if fname.find('/') == -1:
		# no folder = no package for us.
		return ''
	# strip off filename
	x = len(fname) - fname[::-1].find('/')
	fname = fname[:x-1]

	# try to pull out folder
	if fname.find('/') != -1:
		x = len(fname) - fname[::-1].find('/')
		fname = fname[x:]

	return fname

def RollupFunctions(code_lines):
	"""! Go through code looking for functions.

	Note: these are global functions only, not inner or class functions.
	"""

	functions = []

	for line in code_lines:
		# find all lines start with def
		if line.find('def ') == 0:
			s = line.find('def ')
			e = line.find('(')

			name = line[s+4:e]
			functions.append(name)

	return functions

def RollupClasses(code_lines):
	# Go through lines to find class definitions and functions
	# find line numbers for left justified code:
	left = []
	for c,i in zip(code_lines, range(0,len(code_lines))):
		if len(c) > 0 and c[0] != ' ' and c[0] != '\t':
			left.append(i)

	classes = []

	# look for 'class ' lines, then we know which lines contain the class definition:
	for i in left:
		if code_lines[i][:6] == 'class ':
			# get name:
			name = code_lines[i][ 6 : code_lines[i].find('(') ]
			classes.append(name)

	# TODO: find variables?

	return classes

def MakeHeader(fname):
	"""! Add the header block
	"""
	from datetime import datetime

	title = FilenameToTitle(fname)
	package = PackageFromFilename(fname)

	header = HEADER_TEMPLATE.format(title, package)

	from util.util_parsing import MakePostscript
	header = header.replace('[POST]', MakePostscript())

	return header

def BuildHeader(fname, code_lines):
	
	header = MakeHeader(fname)

	text = ''
	if INCLUDE_CLASSES:
		classes = RollupClasses(code_lines)

		if len(classes) > 0:
			text = "## Classes\n"
			for f in classes:
				text += '\t* {}\n'.format(f)
	header = header.replace('[CLASSES]', text)

	text = ''
	if INCLUDE_FUNCTIONS:
		funcs = RollupFunctions(code_lines)

		if len(funcs) > 0:
			text = "## Functions\n"
			for f in funcs:
				text += '\t* {}\n'.format(f)
	header = header.replace('[FUNCTIONS]', text)

	return header

def main():
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		return

	filename = sys.argv[1]

	## if True will replace any existing header documentation with a new auto-generated block.
	FORCE = False
	if True in [x == '-force' for x in sys.argv]:
		FORCE = True

	logger.info('scanning for header in file: {}'.format(filename))

	from py_parsers import ParsePyScript
	code_lines, code_raw = ParsePyScript(filename)

	logger.info('read {} bytes over {} lines of code'.format(len(code_raw),len(code_lines)))

	header = CheckForHeader(code_lines)

	if header != '':
		if FORCE:
			logger.info('removing header...')
			code_raw = RemoveHeader(code_raw)
		else:
			logger.warning('found an existing header, run again with -force to replace with a new auto-gen header.')
			logger.warning(header)
			exit()

	header = BuildHeader(filename, code_lines)
	logger.debug(header)

	if RENAME_ORIGINAL:
		# move original
		os.rename(filename, filename + '.old')
		logger.info('moved original file to {}'.format(filename + '.old'))

	with open(filename, 'w') as f:
		f.write( header + code_raw )
	logger.info('added new header to {}'.format(filename))


if __name__ == '__main__':
	main()