# Andrew Tracey
# 3/14/22
# Topic: Recursion

# I am not too familiar with recursion. The example that intro videos usually
#  start with is factorial. Is it easy to write a program to calculate a
#  factorial without recursion? Let's see.

def fact(n):
	"""Calculate the factorial of n, without recursion"""
	product = 1
	for i in range(1, n + 1):
		product *= i
	return product

# Answer: yes, it is pretty easy but you need a for loop to go through every
#  number from 1 to n. So BigO would be N...is recursion better than that??
# I wouldn't think so...

def fact_r(n):
	"""Use recursion to calculate the factorial of n"""
	if n >= 1:
		return n * fact(n - 1)
	else:
		return 1

print(fact(0), fact_r(0))  # 1
print(fact(1), fact_r(1))  # 1
print(fact(2), fact_r(2))  # 2
print(fact(3), fact_r(3))  # 6
print(fact(4), fact_r(4))  # 24
print(fact(5), fact_r(5))  # 20 x 3 = 60 x 2 = 120
print(fact(7), fact_r(7))  # 120 * 42 = 4,800 + 240 = 5,040
print(fact(10), fact_r(10))
