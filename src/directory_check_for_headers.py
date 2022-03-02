
import os, sys, logging

## go through sub folders as well?
RECURSIVE = True

def TestModulesInDir(path):
	if not path[-1] == '/':
		path += '/'

	from py_parsers import ParsePyScript
	from header_generator import CheckForHeader
	from function_documentor import FindFunctions, CheckForDocumentation
	from util.util_parsing import GetFunctionName

	# get files at path
	children= [os.path.join(path, child) for child in os.listdir(path)]
	directories= list(filter(os.path.isdir, children))

	for f in children:
		if '.py' in f and not '.pyc' in f and not f in directories:

			try:
				code_lines, _ = ParsePyScript(f)
				header = CheckForHeader(code_lines)

				if header is None:
					logging.info('Missing header docstring: {}'.format(f))


				# get all lines that contain a function definition
				func_lines = FindFunctions(code_lines)
				func_lines.append(len(code_lines)) # stick EoF on the list

				for i, j in zip(func_lines[:-1], func_lines[1:]):
					has_doc = CheckForDocumentation(code_lines[i:j])
					if not has_doc:
						logging.info('Missing function docstring: {}::{}'.format(f, GetFunctionName(code_lines[i:j])))
			except:
				logging.error('directory_check_for_headers: {}'.format(f), exc_info = True)

	if RECURSIVE:
		for direct in directories:
			TestModulesInDir(direct)

def main():
	if len(sys.argv) < 2:
		logger.error('missing required directory path')
		return

	path = sys.argv[1]
	
	TestModulesInDir(path)


if __name__ == '__main__':
	main()