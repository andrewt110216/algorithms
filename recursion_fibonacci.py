# Andrew Tracey
# 3/14/22
# Topic: Recursion

# Now, let's try modelling the Fibonacci sequence with and without recursion

# Fibonacci Nums: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# 		 Indexes: 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12 ...

def fib_iterative(n):
	"""Return the nth number of the Fibonacci sequence"""
	if n == 1 or n == 2:
		return 1
	else:
		current, former = 1, 1
		index = 2
		while index < n:
			current, former = current + former, current
			index += 1
		return current

def fib_recursive(n):
	"""Use recursion to return the nth number of the Fibonacci sequence"""
	if n >= 3:
		return fib_recursive(n-1) + fib_recursive(n-2)
	else:  # n = 1 or 2
		return 1

print(fib_recursive(4))  # 3
print(fib_recursive(8))  # 21
print(fib_recursive(12)) # 144
