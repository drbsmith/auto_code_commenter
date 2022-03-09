"""! @file

# Code Line

The basic building block of code. Represents one line of code and the properties and methods for creating and manipulating it.



@package python
"""

from copy import copy
from util.util_parsing import WHITE_SPACE

class CodeLine():
	def __init__(self, line: str):
		if type(line) is str:
			self.line = line
		elif type(line) is CodeLine:
			self.line = line.line
			
		self.type = 'line'
		
		self.indentLevel = None
		# if we ever modify our own line we need to redo this too:
		self.indentLevel = self.getIndentLevel()
		
		self.parent = None
		self.inDocString = False
	def __str__(self):
		return self.line
	def __copy__(self):
		return CodeLine(self.line)
	def __len__(self):
		return len(self.line)
	def find(self, x):
		return self.line.find(x)
		
	def setDocstring(self, flag):
		self.inDocString = flag
		
	def indent(self, tab=None):
		if tab is None:
			return self.line[ : self.getIndentLevel()]
		else:
			if self.inDocString:
				return CodeLine(self.line)
			else:
				line0 = CodeLine.removeLeadingWhitespace(self.line)
				return CodeLine(tab + line0)
				
	def getIndentLevel(self):
		"""! How many indent levels are at the start of this line? """
		if self.line == '':
			return None
		else:
			if not self.indentLevel is None:
				return self.indentLevel
			else:
				# calculate it
				line0 = self.line
				lvl = 0
				while len(line0) > 0 and line0[0] in WHITE_SPACE:
					lvl += 1
					line0 = line0[1:]
				return lvl
				
	def isComment(self):
		line0 = CodeLine.removeLeadingWhitespace(self.line)
		
		if line0 == '':
			return False
		else:
			return (line0[0] == '#' or (len(line0)>2 and (line0[:3] == '"""' or line0[:3] == "'''")))
			
	def split(self, delim=';'):
		if delim in self.line:
			line0 = self.line
			ret = []
			
			# get all occurrences
			idx = [i for i, ltr in enumerate(line0) if ltr == delim]
			
			cum_sum = 0 # use a cumulative sum to adjust indecies as we trim down the string
			for x in idx:
				# is it in a string or comment?
				if not CodeLine.inLiteral(line0, x-cum_sum) and not CodeLine.inComment(line0, x-cum_sum):
					ret.append(CodeLine(line0[:x-cum_sum]))
					line0 = line0[x+1-cum_sum:] # trim the part we are splitting off
					cum_sum += x+1
				else:
					# skip this one ';' but keep ; on looking
					pass
					
			ret.append(CodeLine(line0))
			
			# clean up: set all to the same indent as the first:
			ind = ret[0].indent()
			ret = [x.indent(ind) for x in ret]
			return ret
		else:
			return self.line
			
	def getLastFunctionalPos(self):
		"""! if we have a combined code & comment line, find the last pre-comment, non-white element """
		if self.isComment():
			return 0
		if not '#' in self.line:
			if self.line == '':
				return 0
			else:
				return len(CodeLine.removeTrailingWhitespace(self.line))
		else:
			for i in range(len(self.line)-1, 0, -1):
				if not CodeLine.inComment(self.line, i):
					line0 = self.line[:i+1]
					if len(line0) == 0:
						return 0
					else:
						return len(CodeLine.removeTrailingWhitespace(line0))

	def isFunction(self):
		"""! Test if we are a function definition line """
		return ("def " in self.line and ":" in self.line)
	def isClass(self):
		return ("class " in self.line and ":" in self.line)

	def getFunctionName(self):
		"""!
		pull out the function name from the input function code lines (list of str)
		
		@param func_lines: TODO_DOC
		@return TODO_DOC
		"""
		line = self.line
		if not 'def ' in line:
			return None

		s = line.find('def ')+4
		e = line.find('(')

		return line[s:e].replace(' ', '')
	def getClassName(self):
		"""!
		pull out the class name from our line
		
		@param func_lines: TODO_DOC
		@return the class name
		"""
		line = self.line
		if not 'class ' in line:
			return None

		s = line.find('class ')+5
		e = line.find('(')

		return line[s:e].replace(' ', '')

	def isDecorator(self):
		line0 = CodeLine.removeLeadingWhitespace(self.line)
		if len(line0) > 0 and line0[0] == '@':
			return True
		else:
			return False

	def imports(self):
		"""! Get any packages imported on our line """
		if not self.inDocString and 'import ' in self.line:
			x = self.line.find('import ')
			if not CodeLine.inComment(self.line, x) and not CodeLine.inLiteral(self.line, x):
				# it's a functional import. Now check for a 'from' clause
				if 'from ' in self.line:
					y = self.line.find('from ')
					if x > y:
						return self.line[y+5:x-1]
					# else it is in a comment. ignore it
				else:
					y = self.getLastFunctionalPos() #  if there is a trailing comment on the line we'll ignore it
					return self.line[x+7:y]
		return None
						
	@classmethod
	def inComment(cls, line, pos):
		"""! test if a position in a string is within a comment (or docstring) """
		if pos > len(line) or pos < 0:
			return False
			
		if '#' in line: # test for cases like this, where the # is in a literal, followed by an actual comment
			# sub_lines = CodeLine(line).split('#') # this is a quick solution, but we need to call inComment from split..
			
			# get all occurrences
			ht = [i for i, ltr in enumerate(line) if ltr == '#']
			
			for i in ht:
				# find first hash not in a literal, it must be the start of a comment:
				if not CodeLine.inLiteral(line, i):
					if pos < i:
						return False
					else:
						return True
						
		return False
		
	@classmethod
	def inLiteral(cls, line, pos):
		"""! Test if a specified position in a string is within a string literal.
		Note: Due to the way the in/out signal flips it will report the opening char of a literal as 'out' but the terminating char as 'in'.
		"""
		if pos > len(line) or pos < 0:
			return False
			
		in_literal, literal_type = False, None
		for i in range(0, pos+1):
			if i == pos:
				return in_literal
				
			if (line[i] == '"' or line[i] == "'") and (line[i] == literal_type or literal_type is None):
				in_literal = not in_literal
				if not in_literal:
					literal_type = None
				else:
					literal_type = line[i]
					
		return False
		
	@classmethod
	def removeLeadingWhitespace(cls, line):
		if type(line) is CodeLine:
			line = line.line
		while len(line) > 0 and line[0] in WHITE_SPACE:
			line = line[1:]
			
		return line
		
	@classmethod
	def removeTrailingWhitespace(cls, line):
		if type(line) is CodeLine:
			line = line.line
		while len(line) > 0 and line[-1] in WHITE_SPACE:
			line = line[:-1]
			
		return line
