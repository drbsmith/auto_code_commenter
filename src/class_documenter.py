"""! @file

# Class Documenter

@package src """



## build a profile of each function and include in the documentation
INCLUDE_FUNCTION_PROFILE = True

## pull inline comments up to function docstring
INCLUDE_INLINE_COMMENTS = False

import sys, os

from util.log import setup_logging
logger = setup_logging()

from util.config import GetGlobalConfig
config = GetGlobalConfig()
CLASS_TEMPLATE = config['CLASS_TEMPLATE']

from python_code.CodeLine import CodeLine
from function_documenter import DocumentFunction

def doClassInit(codeblock):	
	# make sure first argument is 'self'. Not a functional requirement, but necessary for doxygen to identify public members
	args = codeblock.getArguments()

	if args[0] != 'self':
		logger.warning('function {} does not have self as first argument in __init__. This will prevent doxygen from finding members.')

	members = codeblock.getMembers(args[0])

	# TODO: we need the line #s and then to stick a new comment line above each...

def main(filename, FORCE):

	with open(filename, 'r') as f:
		raw = f.read()

	from python_code.CodeBlock import CodeBlock
	code_lines = CodeBlock.ParsePython(raw)

	logger.info('read {} bytes over {} blocks of code'.format(len(raw),len(code_lines)))

	write_it = False
	for cb in code_lines:
		if cb.isClass():
			# do all the methods
			methods = cb.getAllFunctions()
			for method in methods:
				if method.getFunctionName() == '__init__':
					doClassInit(method)

				if method.hasDocumentation():
					if FORCE:
						method.removeDocumentation()
					else: continue
				# document each function
				DocumentFunction(method)

			if cb.hasDocumentation():
				if FORCE:
					cb.removeDocumentation()
				else: continue

			# need special handling of __init__ function to document public members

			docs = CLASS_TEMPLATE.split('\n')
			docs = [CodeLine(d) for d in docs]

			cb.addDocumentation(docs)
			write_it = True

	code_lines = code_lines.indent()
	write_it = False

	if write_it:
		# move original
		os.rename(filename, filename + '.old')
		logger.info('moved original file to {}'.format(filename + '.old'))

		with open(filename, 'w') as f:
			f.write( str(code_lines) )

		logger.info('added new class documentation to {}'.format(filename))
	else:
		logger.info('no changes were made.')



if __name__ == "__main__":
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	FORCE = '-force' in sys.argv

	main(filename, FORCE)