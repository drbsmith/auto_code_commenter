"""! @file

# Py Parsers

[Todo: describe what this code file does here, 2022-02-28.]


## Functions
	* ParsePyScript
@package src"""



def ParsePyScript(filename):

	with open(filename, 'r') as f:
		code_raw = f.read()

	# split into lines.
	# TODO: check for different encodings, assuming \n is line ending here:
	code_lines = code_raw.split('\n')

	# if any lines are split over two, join:
	i = 0
	ret = []
	line = ''
	while i < len(code_lines):
		cl = code_lines[i]
		# remove trailing white space
		# TODO: write generic "strip whitespace" function
		while len(cl) > 0 and (cl[-1] == ' ' or cl[-1] == '\t'):
			cl = cl[:-1]

		if line != '':
			# we're appending lines based on a previous trailing \. Strip whitespace, then check that it's not a comment:
			while len(cl) > 0 and (cl[0] == ' ' or cl[0] == '\t'):
				cl = cl[1:]

			if cl[0] == '#' or cl[:3] == '"""' or cl[:3] == "'''":
				i += 1
				continue # skip it, it's a comment

		if len(cl) > 0 and cl[-1] == '\\': # it's a multi-line
			line += cl[:-1]
			# the next line will have a leading indentation, can we strip it with a flag? or test for line != ''?
		else:
			line += cl

			ret.append(line)
			line = ''

		i += 1

	return ret, code_raw

def GetIndent(line):
	"""! return the indentation spacing for the first line
	"""
	# drop empty lines
	# TODO: trap for lines that are whitespace only??
	# lines = [l for l in lines if l != '']

	# get first line indentation
	ind0 = ''
	line0 = line
	while line0[0] == ' ' or line0[0] == '\t':
		ind0 += line0[0]
		line0 = line0[1:]

	# # get second line indent
	# ind1 = ''
	# line1 = lines[1]
	# while line1[0] == ' ' or line1[0] == '\t':
	# 	ind1 += line1[0]
	# 	line1 = line1[1:]

	# while ind0 != '':
	# 	ind0 = ind0[1:]
	# 	ind1 = ind1[1:]

	return ind0