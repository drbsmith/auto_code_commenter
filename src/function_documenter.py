"""! @file

# Function Documentor

Scans a .py file, finds any functions missing documentation blocks, parses variables and inserts boilerplate function documentation.

## Arguments
* -force - overwrite existing function documentation
* -debug - do not write any changes (leaves original file untouched)

## Functions
	* FindFunctions
	* CheckForDocumentation
	* ExtractVariables
	* MakeParamBlock
	* SetIndent
	* BuildFunctionBlock

@package src"""

## build a profile of each function and include in the documentation
INCLUDE_FUNCTION_PROFILE = True

## pull inline comments up to function docstring
INCLUDE_INLINE_COMMENTS = False

import sys, os

from util.log import setup_logging
logger = setup_logging()

from util.config import GetGlobalConfig
config = GetGlobalConfig()
FUNCTION_TEMPLATE = config['FUNCTION_TEMPLATE']
# '''"""!
# TODO_DOC
# [COMMENTS]

# [PARAMS]
# @return TODO_DOC
# [FUNC_PROFILE]
# """
# '''

from python_code.CodeLine import CodeLine
from python_code.CodeBlock import CodeBlock

def FindFunctions(code_lines):
	"""!
	Look through lines of code to find any function definitions.

	@param code_lines: A list of strings, where each is a line of code.

	@return a list of indices where each is a line that contains a 'def ' entry indicating a function definition.
	"""
	# from util.util_parsing import StripLeadingWhitespace
	flines = []

	for line, i in zip(code_lines, range(0,len(code_lines))):
		if line.isFunction():
			flines.append(i)

		# # strip leading white space
		# line = StripLeadingWhitespace(line)

		# # don't use find() because it will pull substrings out of the middle of lines
		# if line[:4] == 'def ':
		# 	flines.append(i)

	return flines

def CheckForDocumentation(func_lines):
	"""!
	Look through the code lines that define a function and check for the presence of a block docstring.

	@param func_lines: (list) lines of code (str) that define a function

	@return True if the docstring is found, False otherwise
	"""

	if len (func_lines) < 2:
		print(func_lines)
		return False
	# TODO: could make this test a global, to catch other styles like ##
	if func_lines[1].find('"""') != -1:
		return True
	else:
		return False

def ExtractComments(func_lines):
	ret = []

	for line in func_lines:
		if '#' in line:
			ret.append('* ' + StripLeadingWhitespace(line.replace('#', '')))

	if len(ret) == 0:
		ret = None
	else:
		ret[0:0] = ['## Comments']
	return ret

def MakeParamBlock(params):
	"""!
	TODO: what does this function do?
	@param params: TODO: what does params variable do?

	@return TODO: what does it return?
	"""
	if params is None or len(params) < 1:
		 return None

	out = []

	for param in params:
		s = CodeLine(config['PARAM_TAG']['value'].format(param) + " TODO_DOC")

		out.append(s)

	return out

def BuildFunctionBlock(name, params=None, profile=None, comments=None, returns=None):
	"""!
	TODO: what does this function do?
	@param indent: TODO: what does indent variable do?
	@param params=None: TODO: what does params=None variable do?

	@return (list) All the lines that make up the documentation block for the function
	"""

	# lines = SetIndent(FUNCTION_TEMPLATE.split('\n'), indent)
	lines = FUNCTION_TEMPLATE.replace('[NAME]', name).split('\n')
	lines = [CodeLine(l) for l in lines]

	# if it returns None we can strip out the @return tag
	if returns is None or returns == []:
		lines = [l for l in lines if not 'return' in l]

	if params is None:
		lines = [l for l in lines if not '[PARAMS]' in l]  # remove the placeholder
	else:
		# inject parameters
		for i in range(0, len(lines)):
			if '[PARAMS]' in lines[i]:
				lines[i:i+1] = params

	if profile is None:
		lines = [l for l in lines if not '[FUNC_PROFILE]' in l]
	else:
		# inject profile
		for i in range(0, len(lines)):
			if '[FUNC_PROFILE]' in lines[i]:
				lines[i:i+1] = profile

	if comments is None:
		lines = [l for l in lines if not '[COMMENTS]' in l]
	else:
		# inject comments
		for i in range(0, len(lines)):
			if '[COMMENTS]' in lines[i]:
				lines[i:i+1] = comments

	return(lines)

def DocumentFunction(codeblock, INCLUDE_FUNCTION_PROFILE=INCLUDE_FUNCTION_PROFILE, INCLUDE_INLINE_COMMENTS=INCLUDE_INLINE_COMMENTS, ignore_args=[]):

	from util.util_parsing import snakeToTitle
	name = codeblock.getFunctionName()
	name = snakeToTitle(name)

	params = codeblock.getArguments()
	params = [p for p in params if not p in ignore_args]
	text = MakeParamBlock(params)

	if INCLUDE_FUNCTION_PROFILE:
		from function_profiler import ProfileFunction, ProfileDictToLines
		profile = ProfileDictToLines(ProfileFunction(codeblock))
	else: profile = None

	if INCLUDE_INLINE_COMMENTS:
		comm = codeblock.getComments()
	else: comm = None

	returns = codeblock.returns()

	docs = BuildFunctionBlock(name, params=text, profile=profile, comments=comm, returns=returns)
	ind = codeblock.indent(None)
	docs = [c.indent(ind) for c in docs]
	
	codeblock.addDocumentation(docs)

def DocumentFunctions(filename, FORCE=False):

	with open(filename, 'r') as f:
		raw = f.read()

	from python_code.CodeBlock import CodeBlock
	code_lines = CodeBlock.ParsePython(raw)

	logger.info('read {} bytes over {} blocks of code'.format(len(raw),len(code_lines)))

	# get all lines that contain a function definition
	# func_lines = FindFunctions(code_lines)
	# func_lines.append(len(code_lines)) # stick EoF on the list
	write_it = False

	# check for all global functions:
	for cb in code_lines:
		if cb.isFunction():
			if cb.hasDocumentation():
				if not FORCE:
					# say something?
					continue
				else:
					cb.removeDocumentation()

			DocumentFunction(cb)
			write_it = True

	code_lines.indent()

	# no changes? don't write anything
	if write_it and not '-debug' in sys.argv:
		# move original
		os.rename(filename, filename + '.old')
		logger.info('moved original file to {}'.format(filename + '.old'))

		with open(filename, 'w') as f:
			f.write( str(code_lines) )
			# for line in code_lines:
			# 	f.write( str(line) )
			# 	f.write( '\n' )
		logger.info('added new function documentation to {}'.format(filename))
	else:
		logger.info('no changes were made.')

if __name__ == "__main__":
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	FORCE = '-force' in sys.argv

	DocumentFunctions(filename, FORCE)
