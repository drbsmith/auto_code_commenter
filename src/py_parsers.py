"""! @file

# Py Parsers

[Todo: describe what this code file does here, 2022-02-28.]


## Functions
	* ParsePyScript
@package src"""



def ParsePyScript(filename):
	"""!
	TODO-DOC: what does this function do?

	@param filename: the path to a .py file to read and parse.

	@return (list) lines of code in the order found in the file,
	@return (string) the raw text read from the file.

	## Profile
	* line count: 52
	* characters: 1400
	* imports: ['from util_parsing import StripTrailingWhitespace, StripLeadingWhitespace']
	* returns: ['@return (list) lines of code in the order found in the file,', "@return (string) the raw text read from the file.'''", 'return ret, code_raw']
	"""

	from util_parsing import StripTrailingWhitespace, StripLeadingWhitespace

	with open(filename, 'r') as f:
		code_raw = f.read()

	# split into lines.
	# TODO: check for different encodings, assuming \n is line ending here:
	code_lines = code_raw.split('\n')

	# if any lines are split over two, join:
	i = 0
	ret = []
	line = ''
	while i < len(code_lines):
		cl = code_lines[i]
		# remove trailing white space
		cl = StripTrailingWhitespace(cl)

		if line != '':
			# we're appending lines based on a previous trailing \. Strip whitespace, then check that it's not a comment:
			cl = StripLeadingWhitespace(cl)

			if cl[0] == '#' or cl[:3] == '"""' or cl[:3] == "'''":
				i += 1
				continue # skip it, it's a comment

		if len(cl) > 0 and cl[-1] == '\\': # it's a multi-line
			line += cl[:-1]
			# the next line will have a leading indentation, can we strip it with a flag? or test for line != ''?
		else:
			line += cl

			# test for compound lines. Note: if the semicolon is inside a text string this will break the code
			while ';' in line:
				s = line.find(';')
				ret.append(line[:s])
				ind = GetIndent(line)
				line = SetIndent(line[s+1:], ind)[0]

			ret.append(line)
			line = ''

		# TODO: move comments on a functional line to the next line

		i += 1

	return ret, code_raw

def GetIndent(line):
	"""!
	TODO-DOC: what does this function do?
	
	@param line: TODO-DOC: what does line variable do?
	@return TODO-DOC: what does it return?
	
	## Profile
	* line count: 24
	* characters: 655
	* imports: ['import util_parsing']
	* returns: ['# return the indentation spacing for the first non-empty line', 'return ind0']
	"""
	
	# return the indentation spacing for the first non-empty line. COULD return an indent for every line included!
	import util_parsing

	# TODO: trap for lines that are whitespace only??
	if type(line) is list:
		# drop empty lines
		line = [l for l in line if l != '']
		line = line[0]

	# get first line indentation
	ind0 = ''
	line0 = line
	while len(line0) > 0 and line0[0] in util_parsing.WHITE_SPACE: # (line0[0] == ' ' or line0[0] == '\t'):
		ind0 += line0[0]
		line0 = line0[1:]

	# # get second line indent
	# ind1 = ''
	# line1 = lines[1]
	# while line1[0] == ' ' or line1[0] == '\t':
	# 	ind1 += line1[0]
	# 	line1 = line1[1:]

	# while ind0 != '':
	# 	ind0 = ind0[1:]
	# 	ind1 = ind1[1:]

	return ind0


def SetIndent(lines, indent):
	"""!
	TODO: what does this function do?
	@param lines: TODO: what does lines variable do?
	@param indent: TODO: what does indent variable do?

	@return TODO: what does it return?
	"""
	from util_parsing import StripLeadingWhitespace 

	if lines is None:
		return None # GIGO
	if indent is None:
		return lines
	if not type(lines) is list: # if it's a single line convert to list
		lines = [lines]

	# strip leading white space from each line, then prepend indent
	ret = []
	for line in lines:
		line = StripLeadingWhitespace(line)
		ret.append(indent + line)

	return ret



