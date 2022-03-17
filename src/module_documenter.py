"""! @file

# Module Documenter

Runs all the documentation generating functions on one file (python module)

## Dependencies
	* header_generator
	* variable_documenter
	* function_documenter
	* sys, os
	* util.log

## Functions
	* main

## Profile
	* number of lines: 54
	* number of characters: 796
	* number of functions: 1

[generated by Auto Code Commenter at 2022-03-17 13:48:17. https://github.com/drbsmith/auto_code_commenter]
@package src """


import sys, os

from util.log import setup_logging
## logger : TODO_DOC
logger = setup_logging()


def main():
	"""!
	# Main
	
	TODO_DOC
	
	@param filename: TODO_DOC
	@param FORCE: TODO_DOC
	@return TODO_DOC
	
	## Profile
	* line count: 12
	* characters: 326
	* imports: variable_documenter, function_documenter, class_documenter, header_generator
	* calls: main, documentVariables, DocumentFunctions, DocumentClasses, AddHeader
	"""
	
	filename = sys.argv[1]
	
	FORCE = '-force' in sys.argv
	
	from variable_documenter import DocumentVariables
	from function_documenter import DocumentFunctions
	from class_documenter import DocumentClasses
	from header_generator import AddHeader
	
	DocumentVariables(filename)
	DocumentFunctions(filename, FORCE)
	DocumentClasses(filename, FORCE)
	AddHeader(filename)
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		logger.error('missing required path to file argument')
		exit()
		
	main()
	
	
	
	
