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
FUNCTION_TEMPLATE = config['FUNCTION_TEMPLATE']



def main(filename, FORCE):

	with open(filename, 'r') as f:
		raw = f.read()

	from python_code.CodeBlock import CodeBlock
	code_lines = CodeBlock.ParsePython(raw)

	logger.info('read {} bytes over {} blocks of code'.format(len(raw),len(code_lines)))

	for cb in code_lines:
		if cb.isClass():
			if cb.hasDocumentation():
				if FORCE:
					cb.removeDocumentation()
				else: continue

			args = cb.getArguments()
			

if __name__ == "__main__":
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	FORCE = '-force' in sys.argv

	main(filename, FORCE)