# TODO Notes

## 2022-03-07

* Tweaks to CodeLine/Block parsing. Handle decorators, incorrect indentation if there is a non-functional ';' in the line. Extra \n after codeblocks when printing (casting to str)
	- docstring start/stop inside of a literal break indentation. They aren't actually starting/closing a docstring but the parser thinks they are...
* Refactor header_generator to use Line/Block parsing
* Refactor directory_check ^
* Refactor function_documentor, function_profiler ^ -- also use config.py for TODO_DOC tags
* CodeBlock.py: indent is being made part of the set_docstrings block. Why??
		This is happening when the previous block is more than one indentation level deeper when it ends. The next code then becomes part of the preceding block, rather than a new block.

---- block vvvv
	def __str__(self):
		ret = ""
---- block vvvv
		for b in self.block:
---- block vvvv
			if type(b) is CodeBlock:
				ret += '---- block vvvv\n'

---- block ^^^^
			ret += '{}\n'.format(str(b)) # the sub block injects its own carriage return and we end up with 2. Maybe check for ending \n in str(b)?
---- block vvvv
			if type(b) is CodeBlock:
				ret += '---- block ^^^^\n'

---- block ^^^^
			return ret
			

---- block ^^^^ <-- this should close 2 blocks, for __str__ and then open a new one, but it grabs the next function before closing.
		def __print__(self):
			print(str(self))

---- block ^^^^