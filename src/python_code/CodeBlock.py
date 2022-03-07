"""! @file

# Code Block

Represents one functional block of code (in python usually indicated with a leading line terminated with a colon ':', and all subsequent lines indented one level).

Q: have one list of all lines/blocks, or split into the 'definition' line and then a list of all sub-items? (the indented lines/blocks)

@package python"""

from python_code.CodeLine import CodeLine

DEFAULT_INDENT = '\t'

class CodeBlock():
	def __init__(self, items):
		self.block = items
		self.type = 'block'
		self.parent = None

		for bl in self.block:
			bl.parent = self
		# self.block = self.indent()
		self._set_docstrings()
	def __str__(self):
		ret = ""
		for b in self.block:
			ret += '{}\n'.format(str(b)) # the sub block injects its own carriage return and we end up with 2. Maybe check for ending \n in str(b)?
		return ret

	def __print__(self):
		print(str(self))
	def __len__(self):
		return len(self.block)
	def __getitem__(self, index):
		return self.block[index]

	def _set_docstrings(self):
		"""! go through our items and tell each one inside a docstring of their membership. """
		docstring = False
		for item in self.block:
			if type(item) is CodeLine:
				item.setDocstring(docstring)
				if '"""' in item.line or "'''" in item.line:
					# if both open and close are in the same line this won't work...
					docstring = not docstring

	def indent(self, tab=''):
		"""! Correct or reformat the indentation of the block. The block does not know if it is inside another block.

		@param self: instance to apply formatting to.
		@param tab=DEFAULT_INDENT: the indentation character to use (usually tab or spaces)
		@return (CodeBlock) the formatted copy of the block 
		"""
		if not tab is None:
			# add tab to each item
			block = [x.indent(tab+DEFAULT_INDENT) for x in self.block]
			# first line has no indentation:
			block[0] = block[0].indent(tab)

			return CodeBlock(block)
		else:
			# GIGO: return the original, unchanged block
			return self.block

	@classmethod
	def __split_lines(cls, lines):
		indents = [l.getIndentLevel() for l in lines]

		items = []
		ind1 = indents[1]
		if ind1 is None: ind1 = 0

		i = 1
		while i < len(lines):
			if indents[i] is None or ind1 == indents[i]:
				items.append(lines[i-1])
				i += 1
			elif indents[i] > ind1:
				item, skip = CodeBlock.__split_lines(lines[i-1:])
				items.append(item)
				i += skip
			else: # indents[i] < ind0:
				items.append(lines[i-1])
				return CodeBlock(items), i

		return CodeBlock(items), i



	@classmethod
	def ParsePython(cls, code):
		from python_code.CodeLine import CodeLine
		# split string of code into str lines, then convert to our helper class
		lines = code.split('\n')
		lines = [CodeLine.removeTrailingWhitespace(l) for l in lines]

		i = 0
		cLines = []
		while i < len(lines):
			line = lines[i]

			if line != '':
				# handle multi line statements with trailing \
				while line[-1] == '\\' and not CodeLine.inComment(line, len(line)-1):
					i += 1
					line = line[:-1] + CodeLine.removeLeadingWhitespace(lines[i])

			# handle midline ;. CodeLine.split takes care of in literals/comments vs functional ;
			# TODO: this appears to add an extra carriage return. Parsing this script puts an extra line ^ there
			if ';' in line:
				sub_lines = CodeLine.split(CodeLine(line), ';')
				cLines += sub_lines
			else:
				cLines.append(line)

			# handle midline # comments. split them to a different line, or just do lots of 'inComment' calls???

			## TODO: handle decorators. Currently they create an extra \n (does every block create that? when it prints?)

			i += 1


		cLines = [CodeLine(l) for l in cLines]


		# group lines into hierarchy of blocks
		# recursive somehow... go down the lines, as long as the indent level is the same between pairs keep collecting, if it changes either
		#  start new collection of indented lines, or return the list (nested lists) we've built
		cb, _ = CodeBlock.__split_lines(cLines)

		#cb = cb.indent()
		print(cb)

		return cb
