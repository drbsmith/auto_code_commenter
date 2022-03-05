
import os
import sys

p = os.path.dirname(os.path.abspath('./src/test'))
sys.path.append(p)


def testCodeLine():
	from python_code.CodeLine import CodeLine

	x = CodeLine('def function():')
	y = CodeLine('	x = 1; y = 2; z = "c"')

	# cast to str
	assert(str(x) == 'def function():')
	assert(str(y) == '	x = 1; y = 2; z = "c"')

	z = y.split()
	assert(len(z) == 3)

	# indent
	assert(y.indent() == '	')
	assert(str(x.indent('  '))[:4] == '  de')

	# isComment
	assert( not x.isComment() )
	x = CodeLine('	# some comments')
	assert( x.isComment() )

	print('CodeLine class passed all tests.')

def testCodeBlock():
	from python_code.CodeLine import CodeLine
	from python_code.CodeBlock import CodeBlock

	s = """def xyz():
	for x in y:
		# do almost nothing
		print(x)
	return None"""
	lines = s.split('\n')
	items = [CodeLine(l) for l in lines]

	loop = CodeBlock(items)

	assert(len(loop) == 5)

	loop1 = loop.indent('\t')
	for l in loop1[1:]:
		assert(str(l)[0] == '\t')

	print(loop.indent())

	assert(str(loop[2]) == '\t\t# do almost nothing')

	print('CodeBlock class passed all tests')

def main():
	with open('./src/python_code/CodeBlock.py', 'r') as f:
		code = f.read()
	from python_code.CodeBlock import CodeBlock

	cb = CodeBlock.ParsePython(code)
	

	testCodeLine()

	testCodeBlock()

if __name__ == '__main__':
	main()