"""! @file

# Util Parsing

Utility functions to help in parsing python code.

## Functions
	* StripLeadingWhitespace
	* StripTrailingWhitespace

@package src"""


WHITE_SPACE = [' ', '\t']

def StripLeadingWhitespace(line: str):
	"""!
	Take off all leading whitespace from a string and return the stripped string.

	@param line: A line of code (str) that might have leading whitespace

	@return the line without any leading whitespace characters
	"""

	while len(line) > 0 and line[0] in WHITE_SPACE:
		line = line[1:]

	return line

def StripTrailingWhitespace(line: str):
	"""!
	Remove any trailing whitespace characters from an input string (line)

	@param line: A string, line of code, that might have trailing whitespace

	@return The input line (str) without any trailing whitespace
	"""

	while len(line) > 0 and line[-1] in WHITE_SPACE:
		line = line[:-1]

	return line

def IsComment(line: str):
	"""!
	TODO-DOC: what does this function do?
	
	@param line:str: TODO-DOC: what does line:str do?
	@return TODO-DOC: what does it return?
	
	## Profile
	* line count: 6
	* characters: 175
	* returns: return True,return False
	"""

	line = StripLeadingWhitespace(line)

	if line[0] == '#' or (len(line)>2 and (line[:3] == '"""' or line[:3] == "'''")):
		return True
	else:
		return False

def StripConsecutiveLineEndings(text):

	while '\n\n\n' in text:
		text = text.replace('\n\n\n', '\n\n')

	return text

