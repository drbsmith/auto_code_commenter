"""! @file

# Init File Creator

Given a directory, checks for a __init__.py and either creates a new one, or replaces the existing one (if -force option is specified).

## Functions
	* GetModules
	* ListToBullets
	* PullOutExisting
	* main

@package src"""

import sys, os

from util.log import setup_logging
logger = setup_logging('init_file_creator.py')

FILE_TEMPLATE = '''"""! @package {}

TODO_DOC

[MODULES]

[POST]

"""'''

def GetModules(files):
	"""!
	Return a list of any files in the input list that match as '.py' files. Ignores files with leading '_'.
	
	@param files: List of file names (path optional)
	@return all file names in the list that match the criteria.
	
	## Profile
	* line count: 3
	* characters: 110
	* returns: return mod
	"""
	

	mod = [f for f in files if (len(f) > 3 and f[-3:] == '.py' and f[0] != '_')]

	return mod

def ListToBullets(files):
	"""!
	Convert a list of file names into a bulleted list (as a string).
	
	@param files: (list) names of files to be compiled into a bullet list in a string.
	@return a string with a well formatted bullet list of file names.
	
	## Profile
	* line count: 7
	* characters: 149
	* returns: return '', return out
	"""
	
	if files is None or len(files) < 1:
		return ''

	out = '## Modules\n\n'
	for f in files:
		out += '* {}\n'.format(f)

	return out

def PullOutExisting(filename):
	"""!
	Given an existing __init__.py file, pull out text that could have been manually entered, between the initial line and our "## Modules" entries.
	
	@param filename: path and filename to the __init__.py file
	@return text pulled out, or None if nothing is found.
	
	## Profile
	* line count: 13
	* characters: 367
	* returns: return out, return None,
	"""
	
	# we found a file that already exists, we pull out everything between the top and our first autogen lines.
	with open(filename, 'r') as f:
		text = f.read()

	lines = text.split('\n')

	for i in range(0, len(lines)):
		if '## Modules' in lines[i]:
			retain = lines[1:i]

			out = ""
			for r in retain:
				out += r + '\n'
			return out

	return None

def main(path):
	"""!
	Main function.
	
	@param path: path of a directory to place a new __init__.py file in.
	@return True on success, False on failure
	
	## Profile
	* line count: 32
	* characters: 1040
	* imports: @see util.util_parsing
	* returns: return False, return True,
	"""
	
	# enforce trailing /
	if not path[-1] == '/':
		path += '/'

	# get files at path
	things = os.listdir(path)

	retain = None
	if '__init__.py' in things:
		if not '-force' in sys.argv:
			logger.info('__init__.py already exists at path {}'.format(path))
			logger.info('run with -force to replace.')
			return False
		else:
			retain = PullOutExisting(path + '__init__.py')
			os.remove(path + '__init__.py')

	logger.info('creating new file at {}__init__.py'.format(path))

	new_file = FILE_TEMPLATE.format(path[:-1])

	if retain:
		new_file = new_file.replace('TODO_DOC', retain)
	else:
		from util.util_parsing import ReplaceTodosWithConfig
		new_file = ReplaceTodosWithConfig(new_file)

	modules = GetModules(things)
	new_file = new_file.replace('[MODULES]', ListToBullets(modules))

	logger.info('adding {} modules to the documentation'.format(len(modules)))

	from util.util_parsing import StripConsecutiveLineEndings, MakePostscript

	new_file = new_file.replace('[POST]', MakePostscript())

	with open(path + '__init__.py', 'w') as f:
		f.write(StripConsecutiveLineEndings(new_file))

	return True

if __name__ == '__main__':
	if len(sys.argv) < 2:
		logger.error('missing required path argument.')
		exit()

	path = sys.argv[1]

	main(path)
