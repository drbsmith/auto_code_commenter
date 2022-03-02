
from util.util_parsing import StripTrailingWhitespace, StripLeadingWhitespace, IsComment

def ProfileFunction(code_lines):
	if len(code_lines) < 1:
		return None
	
	# put together a little dict/statement describing the supplied code.
	out_dict = {}

	# how many lines? Drop any empty lines, they don't count!
	out_dict['line count'] = len([c for c in code_lines if c != ''])

	# how many bytes?
	lengths = [len(line) for line in code_lines]
	out_dict['characters'] = sum(lengths)

	# does it return anything?
	returns = []

	# does it import anything?
	imports = []
	for line in code_lines:
		if 'import' in line and not IsComment(line):
			# what?
			imports.append(StripLeadingWhitespace(line))
		if 'return' in line and not IsComment(line):
			returns.append(StripLeadingWhitespace(line.replace('return', '')))

	if len(imports) > 0:
		out_dict['imports'] = imports
	if len(returns) > 0:
		out_dict['returns'] = returns

	# TODO: find any internal variables??
	# ...

	# TODO: find function calls out?
	# TODO: some estimate of complexity?

	return out_dict

def _list2str(x):
	out = ""

	for y in x:
		out += '{}, '.format(y)

	return out[:-2]

def ProfileDictToLines(profile_dict):
	if profile_dict is None:
		return None	

	# convert each entry to a line of text
	ret = ['', '## Profile']
	for k in profile_dict.keys():
		if not type(profile_dict[k]) is list:
			ret.append('* {}: {}'.format(k, str(profile_dict[k])))
		else:
			ret.append('* {}: {}'.format(k, _list2str(profile_dict[k])))

	return ret