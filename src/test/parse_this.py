
import os
import sys

DEBUG = False

class myclass():

	@classmethod
	def function1():
		# function 1 comment:
		x = 1

		def inner_function(x):
			if '#' in x:
				while '#' in x:
					x.replace('#', '%')

			return x

	def __init__(self, a):
		x = a
if __name__ == '__main__':
	y = myclass()