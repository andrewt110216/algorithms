# April 19, 2022
"""
Produce the first n numbers of the fibonacci sequence iteratively.
"""

def fibonacci(n: int) -> list:
	"""Return a list of the first n fibonacci numbers"""
	
	# Initialize the first two numbers
	fibs = [0, 1]

	# Add additional numbers
	if n >= 3:
		for i in range(2, n):
			fibs.append(fibs[i-1] + fibs[i-2])

	return fibs


if __name__ == '__main__':
	import pprint
	pp = pprint.PrettyPrinter(indent=2, width=40, compact=True)
	pp.pprint((fibonacci(100)))
