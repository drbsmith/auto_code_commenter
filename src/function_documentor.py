"""! @file

# Function Documentor

Scans a .py file, finds any functions missing documentation blocks, parses variables and inserts boilerplate function documentation.


## Functions
	* FindFunctions
	* CheckForDocumentation
	* ExtractVariables
	* MakeParamBlock
	* SetIndent
	* BuildFunctionBlock

@package src"""


INCLUDE_FUNCTION_PROFILE = True

import sys, os

from util.log import setup_logging
logger = setup_logging('function_documentor.py')

FUNCTION_TEMPLATE = '''"""!
TODO_DOC

[PARAMS]
@return TODO_DOC
[FUNC_PROFILE]
"""
'''

from py_parsers import SetIndent, GetIndent

def FindFunctions(code_lines):
	"""!
	Look through lines of code to find any function definitions.

	@param code_lines: A list of strings, where each is a line of code.

	@return a list of indices where each is a line that contains a 'def ' entry indicating a function definition.
	"""

	flines = []

	for line, i in zip(code_lines, range(0,len(code_lines))):
		# strip leading white space
		while len(line) > 0 and (line[0] == ' ' or line[0] == '\t'):
			line = line[1:]
		# don't use find() because it will pull substrings out of the middle of lines
		if line[:4] == 'def ':
			flines.append(i)

	return flines

def CheckForDocumentation( func_lines):
	"""!
	TODO: what does this function do?
	@param func_lines: TODO: what does func_lines variable do?

	@return TODO: what does it return?
	"""

	if len (func_lines) < 2:
		print(func_lines)
		return False
	# TODO: could make this test a global, to catch other styles like ##
	if func_lines[1].find('"""') != -1:
		return True
	else:
		return False

def ExtractVariables(func_lines):
	"""!
	TODO: what does this function do?
	@param func_lines: TODO: what does func_lines variable do?

	@return TODO: what does it return?
	"""

	# func_lines: the definition lines for the whole function
	if func_lines[0][:4] != 'def ':
		logger.error('first line must be the function definition. Instead it is: {}'.format(func_lines[0]))
		return

	# get everything inside of ( )
	s = func_lines[0].find('(') + 1
	e = func_lines[0].find(')')

	var_str = func_lines[0][s:e]
	var = var_str.replace(' ','').split(',')

	logger.debug('found {} variables for function: "{}"'.format(len(var), func_lines[0]))

	return var

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
		s = "@param {}: TODO_DOC".format(param, param)

		out.append(s)

	return out

def BuildFunctionBlock(indent, params=None, profile=None):
	"""!
	TODO: what does this function do?
	@param indent: TODO: what does indent variable do?
	@param params=None: TODO: what does params=None variable do?

	@return (list) All the lines that make up the documentation block for the function
	"""

	lines = SetIndent(FUNCTION_TEMPLATE.split('\n'), indent)

	if params is None:
		lines = [l for l in lines if not '[PARAMS]' in l]
		#block = block.replace('[PARAMS]', '') # remove the placeholder
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

	return(lines)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	from py_parsers import ParsePyScript, GetIndent
	code_lines, code_raw = ParsePyScript(filename)

	logger.info('read {} bytes over {} lines of code'.format(len(code_raw),len(code_lines)))

	# get all lines that contain a function definition
	func_lines = FindFunctions(code_lines)
	func_lines.append(len(code_lines)) # stick EoF on the list

	injects = {}
	# check each function for an existing comment block
	for i, j in zip(func_lines[:-1], func_lines[1:]):
		has_doc = CheckForDocumentation(code_lines[i:j])

		if not has_doc:
			params = ExtractVariables(code_lines[i:j])
			text = MakeParamBlock(params)
			ind = GetIndent(code_lines[i+1:j])
			text = SetIndent(text, ind)

			if INCLUDE_FUNCTION_PROFILE:
				from function_profiler import ProfileFunction, ProfileDictToLines
				profile = ProfileDictToLines(ProfileFunction(code_lines[i:j]))
				profile = SetIndent(profile, ind)

			docs = BuildFunctionBlock(ind, params=text, profile=profile)

			# Lastly, inject our templated doc block!
			injects[i] = docs
			# this is tricky in the raw data... we need to find the def Name( and then the closing ):

	# if we compiled any injects, stick them in from the last backwards to the first
	write_it = False
	if len(injects) > 0:
		idx = list(injects.keys())
		idx.sort(reverse=True)

		for i in idx:
			code_lines[i+1:i+1] = injects[i]
			write_it = True

	# no changes? don't write anything
	if write_it:
		# move original
		os.rename(filename, filename + '.old')
		logger.info('moved original file to {}'.format(filename + '.old'))

		with open(filename, 'w') as f:
			for line in code_lines:
				f.write( line )
				f.write( '\n' )
		logger.info('added new function documentation to {}'.format(filename))
	else:
		logger.info('no changes were made.')

