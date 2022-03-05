"""! @file

# Code Line

The basic building block of code. Represents one line of code and the properties and methods for creating and manipulating it.



@package python
"""

from copy import copy
from util.util_parsing import WHITE_SPACE

class CodeLine():
	def __init__(self, line: str):
		self.line = line
		self.type = 'line'
		self.indentLevel = None
		# if we every modify our own line we need to redo this too:
		self.indentLevel = self.getIndentLevel()
	def __str__(self):
		return self.line
	def __copy__(self):
		return CodeLine(self.line)

	def split(self, delim=';'):
		if delim in self.line:
			line0 = self.line
			ret = []
			while delim in line0:
				x = line0.find(delim)

				ret.append(CodeLine(line0[:x]))
				line0 = line0[x+1:]
			ret.append(CodeLine(line0))
			return ret
		else:
			return self

	def indent(self, tab=None):
		if tab is None:
			return self.line[ : self.getIndentLevel()]
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

		return (line0[0] == '#' or line0[:3] == '"""' or line0[:3] == "'''")

	@classmethod
	def removeLeadingWhitespace(cls, line):
		while len(line) > 0 and line[0] in WHITE_SPACE:
			line = line[1:]

		return line

	@classmethod
	def removeTrailingWhitespace(cls, line):
		while len(line) > 0 and line[-1] in WHITE_SPACE:
			line = line[:-1]

		return line