

@parent_class
class test_class():
	def __init__(self, a, b, c):
		self.a = b
		self.b = c
		self.c = a # rotates assignment to the previous variable

		print('test_class initialized.')

	def function2(self, x):
		# no tricks here, just a function.
		x = 22
		return 42

	def coolFunction(self, d ): # putting a comment inbetween a split line function def like this will break the parsing. Maybe we could write special handlers for it, or we can just say: why? Put your comments in the documentation block!
		print('returning what I got, a {}'.format(d))
		return d

def main():
	# import some generic stuff:
	import sys, os

	x = test_class(1,2,3)

	y = x.coolFunction(4)

	# something about y?
	print(y)

	# don't return anything, but put this keyword in to test the code

if __name__ == '__main__':
	main()

	print('goodbye!')
