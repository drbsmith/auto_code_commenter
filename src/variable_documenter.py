
import logging, sys, os

def main(filename):
	from python_code.CodeBlock import CodeBlock
	from python_code.CodeLine import CodeLine

	## if True will replace any existing variable documentation with new auto-generated lines.
	FORCE = False
	if True in [x == '-force' for x in sys.argv]:
		FORCE = True

	with open(filename, 'r') as f:
		raw = f.read()

	code = CodeBlock.ParsePython(raw)

	variables = [] # keep track of the first appearence of each one
	# check for global variables and see if they have comments
	for i in range(len(code)-1, 0, -1):
		item = code[i]

		if type(item) is CodeBlock:
			continue
		else:
			# it's a root level line. Could it be a variable?
			x = item.find('=')
			if x > -1 and not CodeLine.inLiteral(item.line, x) and not CodeLine.inComment(item.line, x):
				line = CodeLine.removeLeadingWhitespace(item.line)
				var = line[:item.find('=')]

				if not var in variables:
					variables.append(var)

	print(variables)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		logging.error('missing required path to file argument')
		exit()

	filename = sys.argv[1]

	if not os.path.isfile(filename):
		logging.error("{} doesn't exist.".format(filename))
		exit(0)

	main(filename)