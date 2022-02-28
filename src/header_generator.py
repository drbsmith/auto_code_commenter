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


INCLUDE_CLASSES = True
INCLUDE_FUNCTIONS = True

HEADER_TEMPLATE = '''"""! @file

# {}

[Todo: describe what this code file does here, {}.]

@package {}"""
'''

# Rename original: keeps the original source file with a new suffix
RENAME_ORIGINAL = True

import sys, os

from log import setup_logging
logger = setup_logging('header_generator.py')

class headerClass():
	def __init__(self, header):
		self.header = header

def CheckForHeader(lines):
	"""! the header should be the first thing in the file
	Look for a complete comment block 
	"""

	# perform initial cleanup, remove empty lines
	code = [l for l in lines if l != '']

	header = ''
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
			header += x + '\n'

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

def PackageFromFilename(fname):
	"""! if filename has a folder use that as the package designation
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
	"""! Go through lines to find class definitions and functions

	Todo: add properties
	"""
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

	return classes

def MakeHeader(fname):
	"""! Add the header block
	"""
	from datetime import datetime

	title = FilenameToTitle(fname)
	package = PackageFromFilename(fname)

	header = HEADER_TEMPLATE.format(title, datetime.today().strftime('%Y-%m-%d'), package)

	return header

def BuildHeader(fname, code_lines):
	header = MakeHeader(fname)

	text = ''

	if INCLUDE_CLASSES:
		classes = RollupClasses(code_lines)

		text += "\n## Classes\n"
		for f in classes:
			text += '\t* {}\n'.format(f)

	if INCLUDE_FUNCTIONS:
		funcs = RollupFunctions(code_lines)

		text += "\n## Functions\n"
		for f in funcs:
			text += '\t* {}\n'.format(f)

	if text != '':
		x = header.find('@package')

		header = header[:x] + text + header[x:]

	return header

if __name__ == '__main__':
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	FORCE = False
	if True in [x == '-force' for x in sys.argv]:
		FORCE = True

	logger.info('scanning for header in file: {}'.format(filename))

	with open(filename, 'r') as f:
		code_raw = f.read()

	# split into lines.
	# TODO: check for different encodings, assuming \n is line ending here:
	code_lines = code_raw.split('\n')

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

	# move original
	os.rename(filename, filename + '.old')
	logger.info('moved original file to {}'.format(filename + '.old'))

	with open(filename, 'w') as f:
		f.write( header + code_raw )
	logger.info('added new header to {}'.format(filename))
	logger.debug(header)