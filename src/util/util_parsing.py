"""! @file

# Util Parsing

Utility functions to help in parsing python code.

## Functions
	* StripLeadingWhitespace
	* StripTrailingWhitespace

@package src"""

import logging

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
	Test if a string is a python comment.

	TODO: this doesn't check for completion of a triple-quote comment, or if the line is in the middle of a docstring.
	TODO: also build a "comment is in the middle of the string" that catches hash tags within strings, like '# of comments'

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
	"""!
	remove triple line returns and replace with doubles, removes double blank lines
	
	@param text: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 5
	* characters: 196
	* returns: return text
	"""
	
	while '\n\n\n' in text:
		text = text.replace('\n\n\n', '\n\n')

	return text

def GetFunctionName(func_lines):
	"""!
	TODO_DOC
	pull out the function name from the input function code lines (list of str)
	
	@param func_lines: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 10
	* characters: 269
	* returns: return  name
	"""
	
	# pull out the function name from the input function code lines (list of str)

	name = None
	for line in func_lines:
		if 'def ' in line:
			s = line.find('def')+3
			e = line.find('(')

			name = line[s:e].replace(' ', '')

			break
	return name

def ReplaceTodosWithConfig(text):
	"""!
	TODO_DOC
	
	@param text: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 7
	* characters: 289
	* imports: from util.config import GetGlobalConfig
	"""
	
	from util.config import GetGlobalConfig

	config = GetGlobalConfig()

	if not 'TODO_TAG' in config:
		logging.warning('config does not contain TODO_TAG, not updating the default todo marker.')
	else:
		text = text.replace('TODO_DOC', config['TODO_TAG']['value'])

def MakePostscript():
	"""!
	TODO_DOC
	could be moved to a different module. Not really strictly a parsing util
	
	@param : TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 6
	* characters: 294
	* imports: from datetime import datetime
	* returns: return ps
	"""

	# could be moved to a different module. Not really strictly a parsing util
	from datetime import datetime

	ps = "[generated by Auto Code Commenter at {}. https://github.com/drbsmith/auto_code_commenter]"
	ps = ps.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

	return ps



