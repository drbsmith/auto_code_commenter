

import sys, os

from log import setup_logging
logger = setup_logging('function_documentor.py')

FUNCTION_TEMPLATE = '''"""!
TODO: what does this function do?
@return TODO: what does it return?
"""
'''

def FindFunctions(code_lines):
	flines = []

	for line, i in zip(code_lines, range(0,len(code_lines))):
		# strip leading white space
		while len(line) > 0 and (line[0] == ' ' or line[0] == '\t'):
			line = line[1:]
		# don't use find() because it will pull substrings out of the middle of lines
		if line[:4] == 'def ':
			flines.append(i)

	return flines

def CheckForDocumentation( \
	# this is a comment in the middle of a function def
	func_lines):
	if len (func_lines) < 2:
		print(func_lines)
		return False
	# TODO: could make this test a global, to catch other styles like ##
	if func_lines[1].find('"""') != -1:
		return True
	else:
		return False

def ExtractVariables(func_lines):
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
	out = []

	for param in params:
		s = "@param {}: TODO: what does this variable do?".format(param)

		out.append(s)

	return out

def SetIndentation(lines, indent):
	# strip leading white space from each line, then prepend indent
	ret = []
	for line in lines:
		while len(line) > 0 and (line[0] == ' ' or line[0] == '\t'):
			line = line[1:]
		ret.append(indent + line)

	return ret

def BuildFunctionBlock(indent, params=None):
	block = FUNCTION_TEMPLATE

	if params != None:
		# inject parameters
		x = block.find('@return')

		p_str = ""
		for p in params:
			p_str += p + '\n'

		block = block[:x] + p_str + block[x:]

	# split to lines, set indentation, then reassemble as text blob
	lines = SetIndentation(block.split('\n'), indent)
	block = ""
	for l in lines:
		block += l + '\n'

	print(block)
	return(block)

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

	# check each function for an existing comment block
	for i, j in zip(func_lines[:-1], func_lines[1:]):
		has_doc = CheckForDocumentation(code_lines[i:j])

		if not has_doc:
			params = ExtractVariables(code_lines[i:j])
			text = MakeParamBlock(params)
			text = SetIndentation(text, GetIndent(code_lines[i+1]))

			BuildFunctionBlock(GetIndent(code_lines[i+1]), params=text)

			# Lastly, inject our templated doc block!