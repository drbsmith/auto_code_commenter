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
			if type(b) is CodeBlock:
				ret += '---- block vvvv\n'
			ret += '{}\n'.format(str(b)) # the sub block injects its own carriage return and we end up with 2. Maybe check for ending \n in str(b)?
			if type(b) is CodeBlock:
				ret += '---- block ^^^^\n'
		return ret

	def __print__(self):
		print(str(self))
	def __len__(self):
		return len(self.block)
	def __getitem__(self, index):
		return self.block[index]

	def _set_docstrings(self):
		"""! go through our items and tell each one inside a docstring of their membership. """

		docs = ['"""', "'''"] # the two variants of doc string tags
		docstring = False
		for item in self.block:
			if type(item) is CodeLine:
				item.setDocstring(docstring)
				for tag in docs:
					if tag in item.line:
						line0 = item.line

						# count how many times they show up. Even is closed (or reopened), odd is opening
						ct = 0
						while tag in line0:
							x = line0.find(tag)
							if not CodeLine.inLiteral(line0, x):
								ct += 1
							line0 = line0[x+3:]

						if ct % 2 == 1:
							docstring = not docstring
							break # have to check the other one... but it could be inside??
						else: # it has a complete string in one line (or it closes and opens again). If it opens another one on the outside... just say we can't handle it?
							break

	def indent(self, tab=''):
		"""! Correct or reformat the indentation of the block. The block does not know if it is inside another block.

		@param self: instance to apply formatting to.
		@param tab=DEFAULT_INDENT: the indentation character to use (usually tab or spaces)
		@return (CodeBlock) the formatted copy of the block 
		"""
		if not tab is None:
			# add tab to each item
			block = []
			for item in self.block:
				block.append(item.indent(tab))

				# trailing colon, specifying an indented block?
				if type(item) is CodeLine and len(item) > 0 and not item.inDocString:
					s = item.line[:item.getLastFunctionalPos()]
					if s[-1] == ':':
						tab += DEFAULT_INDENT

			# block = [x.indent(tab+DEFAULT_INDENT) for x in self.block]
			# # first line has no indentation:
			# block[0] = block[0].indent(tab)

			return CodeBlock(block)
		else:
			# GIGO: return the original, unchanged block
			return self.block

	@classmethod
	def __split_lines(cls, lines):
		"""! 
		@param lines: list of strings to parse
		@return (CodeBlock, int) The root CodeBlock and a count of how many lines were processed. 
		"""

		# method based on indentation levels.
		indents = [l.getIndentLevel() for l in lines]

		items = []
		ind1 = indents[0]
		if ind1 is None: ind1 = 0

		for ind, line, i in zip(indents, lines, range(0,len(lines))): # find first inset line
			if ind is None or ind == ind1: # get all the same indent, define lines
				items.append(line)
			elif ind != ind1 and not ind is None:
				ind1 = ind
				break

		i += 1
		while i < len(lines):
			if indents[i] is None or ind1 == indents[i]:
				items.append(lines[i-1])
				i += 1
			elif indents[i] < ind1:
				items.append(lines[i-1])
				return CodeBlock(items), i
			else:  #indents[i] > ind1:
				cl = CodeLine(lines[i-1])
				if len(cl) > 0 and cl.line[:cl.getLastFunctionalPos()][-1] == ':':
					idx = i-1 # check for preceding decorators
					while indents[idx] == indents[idx-1] and CodeLine.removeLeadingWhitespace(lines[idx-1])[0] == '@':
						idx -= 1

					item, skip = CodeBlock.__split_lines(lines[idx:])
					items.append(item)
					i += skip

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

			# TODO: this appears to add an extra carriage return. Parsing this script puts an extra line here, and indents this comment incorrectly. Taking out these comments indents the if line wrong.
			if ';' in line:
				# handle midline ;. CodeLine.split takes care of in literals/comments vs functional ;
				sub_lines = CodeLine.split(CodeLine(line), ';')
				cLines += sub_lines
			else:
				cLines.append(line)

			# handle midline # comments. split them to a different line, or just do lots of 'inComment' calls???


			i += 1

		cLines = [CodeLine(l) for l in cLines]


		# group lines into hierarchy of blocks
		# recursive somehow... go down the lines, as long as the indent level is the same between pairs keep collecting, if it changes either
		#  start new collection of indented lines, or return the list (nested lists) we've built
		cb, _ = CodeBlock.__split_lines(cLines)

		cb = cb.indent()
		print(cb)

		return cb
