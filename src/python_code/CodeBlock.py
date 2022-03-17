"""! @file

# Code Block

Represents one functional block of code (in python usually indicated with a leading line terminated with a colon ':', and all subsequent lines indented one level).

Q: have one list of all lines/blocks, or split into the 'definition' line and then a list of all sub-items? (the indented lines/blocks)

@package python"""

import logging
from python_code.CodeLine import CodeLine

## DEFAULT_INDENT : the indentation literal to use in indenting cobe blocks
DEFAULT_INDENT = '\t'

## DEBUG : If True will cause extra prints and text added to string conversions
DEBUG = False

class CodeBlock():
	"""!
	TODO_DOC
	
	[MEMBERS]
	[CLASS_PROFILE]
	"""
	
	def __init__(self, items):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@param items: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 12
		* characters: 349
		"""
		
		## (list) all of the elements that make up our block of code.
		self.block = items
		## TODO_DOC: what is type class member variable?
		self.type = 'block'
		## TODO_DOC: what is parent class member variable?
		self.parent = None
		
		for bl in self.block:
			bl.parent = self
		# self.block = self.indent()
		self._set_docstrings()
	def __str__(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 13
		* characters: 342
		* returns: ret
		"""
		
		ret = ""
		for b in self.block:
			if type(b) is CodeBlock:
				if DEBUG:
					ret += '#### block vvvv\n'
				ret += str(b)
				if DEBUG:
					ret += '#### block ^^^^\n'
			else:
				ret += '{}\n'.format(str(b)) # the sub block injects its own carriage return and we end up with 2. Maybe check for ending \n in str(b)?
		return ret
		
	def __print__(self):
		"""! @param self: instance to print. """
		print(str(self))
	def __len__(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 2
		* characters: 43
		* returns: len(self.block)
		"""
		
		return len(self.block)
	def __getitem__(self, index):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@param index: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 2
		* characters: 56
		* returns: self.block[index]
		"""
		
		return self.block[index]
	def delete(self, start, end):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@param start: TODO_DOC
		@param end: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 2
		* characters: 57
		"""
		
		del self.block[start:end]
	def find(self, what):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@param what: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 7
		* characters: 186
		* returns: -1
		"""
		
		# would we actually recursively search, or just return "nope"?
		# for item in self.block:
		# 	x, it = item.find(what)
		# 	if x != -1:
		# 		return x, it
		return -1
	def insert(self, i, x):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@param i: TODO_DOC
		@param x: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 5
		* characters: 80
		"""
		
		if not type(x) is list:
			x = [x]
		self.block[i:i] = x
		
	def getTotalLines(self):
		"""! how many lines in total are within our block? """
		total = [item.getTotalLines() if type(item) is CodeBlock else 1 for item in self.block]
		return sum(total)
	def getTotalBytes(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC
		"""
		
		total = [item.getTotalBytes() if type(item) is CodeBlock else len(item) for item in self.block]
		return sum(total)
		
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
		Makes the change in place and also returns itself for . chaining code.

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
					if len(s) > 0 and s[-1] == ':':
						tab += DEFAULT_INDENT
						
			self.block = block
			return self
		else:
			# return first not '' indent:
			for item in self.block:
				ind = item.indent(None)
				if not ind is None and not ind == '':
					return ind
					
	def isFunction(self):
		"""!
		TODO_DOC
		
		@return TODO_DOC
		
		## Profile
		* line count: 7
		* characters: 262
		* returns: False, True
		"""
		
		for item in self.block:
			# if we hit a line that is not empty, a decorator, or is function we return false
			if len(item) != 0 and not item.isDecorator() and not item.isFunction():
				return False
			elif item.isFunction():
				return True
	def getFunctionName(self):
		"""!
		TODO_DOC
		
		@return TODO_DOC
		
		## Profile
		* line count: 5
		* characters: 110
		* returns: name
		"""
		
		for item in self.block:
			name = item.getFunctionName()
			if name:
				return name
	def getArguments(self):
		"""! if we're a class or function, pull out the arguments """
		for item in self.block:
			if item.isFunction() or item.isClass():
				args = item.getArguments()
				
				logging.debug('found {} arguments for function: "{}"'.format(len(args), item))
				return args
		else: return None

	def isClass(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 7
		* characters: 253
		* returns: False, True
		"""
		
		for item in self.block:
			# if we hit a line that is not empty, a decorator, or is function we return false
			if len(item) != 0 and not item.isDecorator() and not item.isClass():
				return False
			elif item.isClass():
				return True
	def getClassName(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 6
		* characters: 104
		* returns: name
		"""
		
		for item in self.block:
			name = item.getClassName()
			if name:
				return name
				
	def imports(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 7
		* characters: 160
		* imports: util.util_parsing
		* returns: ret
		"""
		
		from util.util_parsing import flatten
		
		ret = [x.imports() for x in self.block]
		ret = [r for r in ret if r]
		ret = flatten(ret)
		return ret
	def returns(self):
		"""!
		TODO_DOC

		@param self: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 8
		* characters: 160
		* imports: util.util_parsing
		* returns: ret
		"""
		
		from util.util_parsing import flatten
		
		ret = [x.returns() for x in self.block]
		ret = [r for r in ret if r]
		ret = flatten(ret)
		return ret
		
	# ----
	def getAllFunctions(self):
		"""! Look through our block and pull out any sub-function blocks. Usually used by classes. """
		ret = []
		for item in self.block:
			if type(item) is CodeBlock and item.isFunction():
				# return the collection of all function blocks. They can be modified externally.
				ret.append(item)
		if len(ret) > 0:
			return ret
		else: return None
		
	def getMembers(self, cls='self'):
		"""! if we are a function within a class, look for members with the pattern 'cls.x' """
		from util.util_parsing import flatten
		
		ret = [item.getMembers(cls) for item in self.block]
		ret = [r for r in ret if r]
		ret = flatten(ret)
		# convert to set to get distinct values, then back to list
		return list(set(ret))

	def getCalls(self):
		"""! find any function calls in the block and return those functions. 
		"""
		from util.util_parsing import flatten
		
		ret = [item.getCalls() for item in self.block]
		ret = [r for r in ret if r]
		ret = flatten(ret)
		return ret

		
	# --- Documentation methods ---- #
	
	def hasDocumentation(self):
		"""! Does our block have a doc string in it? """
		for item in self.block:
			if item.find('"""!') > -1:
				return True
		return False
	def removeDocumentation(self):
		"""! if we have documentation, remove it. """
		if not self.hasDocumentation():
			return False
		else:
			s, e = 0, -1
			for x, i in zip(self.block, range(0,len(self.block))):
				if x.find('"""!') > -1:
					s = i
				elif x.find('"""') > -1:
					e = i + 1
					break
					
			if e > s:
				del self.block[s:e]
				return True
		return False
	def addDocumentation(self, lines):
		"""! take new docstring lines and insert. Relies on calling function to remove other docs and not call this incorrectly. """
		# walk down to first actual code line
		found_it = False
		for item, i in zip(self.block, range(0, len(self.block))):
			# only skip comments if they are pre the def/class: line
			if not type(item) is CodeBlock and ((item.isComment() and not found_it) or item.isDecorator() or item.isClass() or item.isFunction()):
				if item.isFunction() or item.isClass():
					found_it = True # don't count any more comments. We'll inject the docstring there
				continue
				
			self.block[i:i] = lines
			return True
			
	def getComments(self):
		"""! Collect any whole line comments and return as a list """
		ret = []
		for item in self.block:
			if type(item) is CodeLine:
				if item.isComment():
					ret.append(item)
			else:
				c = item.getComments()
				if c: ret += c
				
		if len(ret) > 0:
			return ret
		else: return None
		
	@classmethod
	def __split_module(cls, lines):
		"""!
		TODO_DOC

		@param cls: TODO_DOC
		@param lines: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 29
		* characters: 802
		* returns: CodeBlock(items), i
		"""
		
		items = []
		indents = [l.getIndentLevel() for l in lines]
		
		i = 0
		try:
			while i < len(lines):
				cl = CodeLine(lines[i])
				lfchar = cl.line[:cl.getLastFunctionalPos()]
				if len(lfchar) > 0 and lfchar[-1] == ':':
					idx = i # check for preceding decorators
					while indents[idx] == indents[idx-1] and (len(lines[idx-1])==0 or CodeLine.RemoveLeadingWhitespace(lines[idx-1])[0] == '@'):
						idx -= 1
						i -= 1
						items.pop() # remove the last line because we're passing it to the next block
					item, skip = CodeBlock.__split_lines(lines[idx:])
					items.append(item)
					i += skip
				else: # indents[i] is None or indents[i] == 0:
					items.append(lines[i])
					i += 1
					
			return CodeBlock(items), i
		except:
			logging.error(lines[i], exc_info=True)
			
			
			
	@classmethod
	def __split_lines(cls, lines):
		"""!
		In building this, a couple special cases have emerged:
			* When its the root block, with lots of left aligned code/imports/comments
			* when it's a class/function def with a line or two (decorators) at one indentation and all the rest in one more
			
			@param lines: list of strings to parse
			@return (CodeBlock, int) The root CodeBlock and a count of how many lines were processed.
			"""
		indents = [l.getIndentLevel() for l in lines]

		# get the block's def indentation
		items = []
		ind0 = indents[0]
		if ind0 is None: # find first not None indent
			for ind in indents:
				if not ind is None:
					ind0 = ind
					break
					
		# get the block def lines and find the block content indentation
		ind1 = None
		for ind, line, i in zip(indents, lines, range(0,len(lines))): # walk to the first indented line
			if ind is None or ind == ind0: # get all the same indent, define lines
				items.append(line)
			elif ind > ind0: # we're in the content lines for this block
				ind1 = ind
				break
				
		# ind0 is the start indentation, ind1 is the content indent. ind1 is None when there are no indented lines.
		if not ind1 is None:
			while i < len(lines):
				cl = CodeLine(lines[i])
				
				if not indents[i] is None and indents[i] < ind1:
					return CodeBlock(items), i 	# block ended, return
				else:
					lfchar = cl.line[:cl.getLastFunctionalPos()]
					
					if len(lfchar) > 0 and lfchar[-1] == ':':
						# check if it's a new function/block
						idx = i # check for preceding decorators
						while indents[idx] == indents[idx-1] and CodeLine.RemoveLeadingWhitespace(lines[idx-1])[0] == '@':
							idx -= 1
							i -= 1
							items.pop() # remove the last line because we're passing it to the next block
							
						item, skip = CodeBlock.__split_lines(lines[idx:])
						items.append(item)
						i += skip
					else:
						items.append(lines[i])
						i += 1
						
		return CodeBlock(items), i



	@classmethod
	def ParsePython(cls, code):
		"""!
		TODO_DOC

		@param cls: TODO_DOC
		@param code: TODO_DOC
		@return TODO_DOC

		## Profile
		* line count: 47
		* characters: 1452
		* imports: python_code.CodeLine
		* returns: cb
		"""
		
		from python_code.CodeLine import CodeLine
		# split string of code into str lines, then convert to our helper class
		lines = code.split('\n')
		lines = [CodeLine.RemoveTrailingWhitespace(l) for l in lines]
		
		# print(code, '\n')
		
		i = 0
		cLines = []
		while i < len(lines):
			line = lines[i]
			
			if line != '':
				# handle multi line statements with trailing \
				while line[-1] == '\\' and not CodeLine.inComment(line, len(line)-1):
					i += 1
					line = line[:-1] + CodeLine.RemoveLeadingWhitespace(lines[i])
					
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
		cb, _ = CodeBlock.__split_module(cLines)
		
		# cb = cb.indent()
		# print(cb)
		
		return cb
		
		
		
