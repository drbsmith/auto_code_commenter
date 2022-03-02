



import sys, os

from util.log import setup_logging
logger = setup_logging('init_file_creator.py')

FILE_TEMPLATE = '''"""! @package {}

TODO-DOC

[MODULES]

"""'''

def GetModules(files):

	mod = [f for f in files if (len(f) > 3 and f[-3:] == '.py' and f[0] != '_')]

	return mod

def ListToBullets(files):
	if files is None or len(files) < 1:
		return ''

	out = '## Modules\n\n'
	for f in files:
		out += '* {}\n'.format(f)

	return out

def PullOutExisting(filename):
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
		new_file = new_file.replace('TODO-DOC', retain)

	modules = GetModules(things)
	new_file = new_file.replace('[MODULES]', ListToBullets(modules))

	logger.info('adding {} modules to the documentation'.format(len(modules)))

	from util.util_parsing import StripConsecutiveLineEndings

	with open(path + '__init__.py', 'w') as f:
		f.write(StripConsecutiveLineEndings(new_file))

	return True

if __name__ == '__main__':
	if len(sys.argv) < 2:
		logger.error('missing required path argument.')
		exit()

	path = sys.argv[1]

	main(path)