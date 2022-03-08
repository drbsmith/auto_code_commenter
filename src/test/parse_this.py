

class myclass():

	@classmethod
	def function1():
		# function 1 comment:
		x = 1

		def inner_function():
			x += 1
			return x

	def __init__(self, a):
		x = a

if __name__ == '__main__':
	y = myclass()