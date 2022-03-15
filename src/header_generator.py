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

INCLUDE_PACKAGES = True

## Template used to generate the header block.
# TODO: move to a file that can be specified without modifying this code.

from util.config import GetGlobalConfig
config = GetGlobalConfig()
HEADER_TEMPLATE = config['HEADER_TEMPLATE']

# HEADER_TEMPLATE = '''"""! @file

# # {}

# TODO_DOC

# [PACKAGES]
# [CLASSES]
# [FUNCTIONS]
# [POST]
# @package {}"""

# '''

## Rename original: keeps the original source file with a new suffix
RENAME_ORIGINAL = True

import sys, os

from util.log import setup_logging
logger = setup_logging('header_generator.py')


def CheckForHeader(code):
	"""! the header should be the first thing in the file
	Look for a complete comment block
	"""

	# perform initial cleanup, remove empty lines
	# code = [l for l in lines if l != '']

	header = None
	exists = False
	for x in code:
		if exists:
			header.append(x)
			if x.find('"""') > -1: # end of header
				break
		# do this test second to not trigger end test
		if x.find('"""!') > -1:
			# fully left justified comment block. Should be the file header, but could it be somewhere else in the file?
			exists = True
			header = [x]

	return header

def RemoveHeader(code):
	"""!
	TODO_DOC
	
	@param code: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 15
	* characters: 216
	* returns: code
	"""
	
	s, e = 0, -1
	for x, i in zip(code, range(0,len(code))):
		if x.find('"""!') > -1:
			s = i
		elif x.find('"""') > -1:
			e = i + 1
			break

	code.delete(s, e)

	# ret = code[:s] + code[e:]

	return code

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

	for item in code_lines:
		# find all lines start with def
		if item.isFunction():
			name = item.getFunctionName()
			functions.append(name)

	return functions

def RollupClasses(code_lines):
	# Go through lines to find class definitions
	"""!
	TODO_DOC
	
	@param code_lines: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 15
	* characters: 256
	* returns: classes
	"""
	

	classes = []

	for item in code_lines:
		# find all lines start with def
		if item.isClass():
			name = item.getClassName()
			classes.append(name)

	# TODO: find variables?

	return classes

def RollupPackages(code_lines):
	"""!
	TODO_DOC
	
	@param code_lines: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 8
	* characters: 203
	* imports: 	from util.util_parsing import flatten, 	packages = [item.imports() for item in code_lines]
	* returns: packages
	"""
	
	from util.util_parsing import flatten
	packages = [item.imports() for item in code_lines]
	packages = [p for p in packages if p]
	packages = flatten(packages)

	return packages

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
	"""!
	TODO_DOC
	
	@param fname: TODO_DOC
	@param code_lines: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 36
	* characters: 710
	* returns: header
	"""
	

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

	text = ''
	if INCLUDE_PACKAGES:
		imports = RollupPackages(code_lines)

		if len(imports) > 0:
			text = "## Dependencies\n"
			for i in imports:
				text += '\t* {}\n'.format(i)
	header = header.replace('[PACKAGES]', text)

	return header

def main():
	"""!
	TODO_DOC
	
	@param : TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 46
	* characters: 1249
	* imports: 	from python_code.CodeBlock import CodeBlock
	"""
	
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		return

	filename = sys.argv[1]

	## if True will replace any existing header documentation with a new auto-generated block.
	FORCE = False
	if True in [x == '-force' for x in sys.argv]:
		FORCE = True

	logger.info('scanning for header in file: {}'.format(filename))

	with open(filename, 'r') as f:
		rawcode = f.read()

	from python_code.CodeBlock import CodeBlock
	code_module = CodeBlock.ParsePython(rawcode)

	logger.info('read {} lines of code at root'.format(len(code_module)))

	header = CheckForHeader(code_module)

	if not header is None:
		if FORCE:
			logger.info('removing header...')
			code_module = RemoveHeader(code_module)
		else:
			logger.warning('found an existing header, run again with -force to replace with a new auto-gen header.')
			logger.warning(CodeBlock(header))  # cast list as CodeBlock to pretty print lines
			exit()

	header = BuildHeader(filename, code_module)
	logger.debug(header)

	if RENAME_ORIGINAL:
		# move original
		os.rename(filename, filename + '.old')
		logger.info('moved original file to {}'.format(filename + '.old'))

	with open(filename, 'w') as f:
		f.write( header + str(code_module) )
	logger.info('added new header to {}'.format(filename))


if __name__ == '__main__':
	main()
