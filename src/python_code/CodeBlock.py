"""! @file

# Code Block

Represents one functional block of code (in python usually indicated with a leading line terminated with a colon ':', and all subsequent lines indented one level).

Q: have one list of all lines/blocks, or split into the 'definition' line and then a list of all sub-items? (the indented lines/blocks)

@package python"""

from copy import copy

DEFAULT_INDENT = '\t'

class CodeBlock():
	def __init__(self, items):
		self.block = items
		self.type = 'block'

		# self.block = self.indent()
	def __str__(self):
		ret = ""
		for b, i in zip(self.block, range(0,len(self.block))):
			ret += '{}:{}\n'.format(i,str(b))
		return ret

	def __print__(self):
		print(str(self))
	def __len__(self):
		return len(self.block)
	def __getitem__(self, index):
		return self.block[index]

	def indent(self, tab=''):
		"""! Correct or reformat the indentation of the block. The block does not know if it is inside another block.

		@param self: instance to apply formatting to.
		@param tab=DEFAULT_INDENT: the indentation character to use (usually tab or spaces)
		@return (CodeBlock) the formatted copy of the block 
		"""
		if not tab is None:
			# try:
			# add tab to each items already indent
			block = [x.indent(tab+DEFAULT_INDENT) for x in self.block]
			# first line has no indentation:
			block[0] = block[0].indent(tab)

			# self.block = block
			return CodeBlock(block)
			# except AttributeError:
			# 	print("AttributeError")
			# 	print(self.block)
			# 	return self.block

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
				print(type(item))
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
		cLines = [CodeLine(l) for l in lines]

		# group lines into hierarchy of blocks
		# recursive somehow... go down the lines, as long as the indent level is the same between pairs keep collecting, if it changes either
		#  start new collection of indented lines, or return the list (nested lists) we've built
		cb, _ = CodeBlock.__split_lines(cLines)

		cb = cb.indent()
		print(cb)

		return cb
