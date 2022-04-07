# Andrew Tracey
# 3/23/22
# Topic: Recursive Solution to Karatsuba Integer Multiplication

# Worked on this after the example was presented as an algorithm in the
#  intro for the Stanford Algorithms course on Coursera.
# Note: this solution is not technically Karatsuba because it uses 4 
#  recursive calls instead of 3.

# ONLY WORKS FOR NUMBERS WITH UP TO 15 DIGITS...not sure why.


from random import randrange
from math import ceil


def random_ndigit_ints(n):
	"""Get a random integer with n digits"""
	return (
		randrange(10**(n-1), 10**n),
		randrange(10**(n-1), 10**n)
		)

def karatsuba(x, y, layer=0):
	"""
	Return the product of two even integers using Karatsuba Multiplication.
	"""

	# Convert x and y into strings
	layer += 1
	x = str(int(x))
	y = str(int(y))

	# Determine the length that both integers should be
	n = max(len(x), len(y))

	# Pad 0's in front of the integers, if needed
	if len(x) > len(y):
		y = '0' * (len(x) - len(y)) + y
	elif len(y) > len(x):
		x = '0' * (len(y) - len(x)) + x

	if debug: print(f" |{' '*layer*4}Starting Karatsuba for {x} and {y}...")

	# Base Case: If n = 1, then use basic operation of single digit mult.
	if n == 1:
		if debug: print(f" |{' '*layer*4}> Result: {int(x) * int(y):,}")
		return int(x) * int(y)
	# Otherwise, recurisvely use Karatsuba Algorithm
	else:
		# Split x and y into two smaller numbers
		mid = ceil(n / 2)
		a = x[:mid]
		b = x[mid:]
		c = y[:mid]
		d = y[mid:]
		if debug: print(f" |{' '*layer*4}\ta-b-c-d =", 
			a + "-" + b + "-" + c + "-" + d)

		# Call Karatsuba to calculate the smaller products required
		ac = karatsuba(int(a), int(c), layer)
		bd = karatsuba(int(b), int(d), layer)
		ad = karatsuba(int(a), int(d), layer)
		bc = karatsuba(int(b), int(c), layer)

		# Final step to calculate product
		if n % 2 == 0:  # n is even
			prod = ac*10**n + (ad + bc)*10**(n/2) + bd
		else:  # n is odd
			prod = ac*10**(2*mid-2) + (ad + bc)*10**(mid-1) + bd
		if debug: print(f" |{' '*layer*4}> Result: {int(prod):,}")
		return int(prod)


# -------------------------------- TEST CASES --------------------------------

# ============================================================================
# Set to true to see debugging print statements from function execution
debug = False
# ============================================================================

tests = 0
failed_tests = 0

n = 4
print(f"============== TEST CASE: n = {n} ==============")
for _ in range(2):
	tests += 1
	x, y = random_ndigit_ints(n)
	print(f"Calculating product of {x:,} and {y:,}...")
	product = karatsuba(x, y)
	print(f" | FINAL RESULT: {x:,} x {y:,} = {product:,}")
	if product == x * y:
		print(" | **CORRECT**")
	else:
		print(" | **WRONG**")
		failed_tests += 1
	print(" | \n")

n = 7
print(f"============== TEST CASE: n = {n} ==============")
for _ in range(2):
	tests += 1
	x, y = random_ndigit_ints(n)
	print(f"Calculating product of {x:,} and {y:,}...")
	product = karatsuba(x, y)
	print(f" | FINAL RESULT: {x:,} x {y:,} = {product:,}")
	if product == x * y:
		print(" | **CORRECT**")
	else:
		print(" | **WRONG**")
		failed_tests += 1
	print(" | \n")


n = 15  # ONLY WORKS WITH N UP TO 15...not sure why :( 
print(f"============== TEST CASE: n = {n} ==============")
for _ in range(2):
	tests += 1
	x, y = random_ndigit_ints(n)
	print(f"Calculating product of {x:,} and {y:,}...")
	product = karatsuba(x, y)
	print(f" | \n | FINAL RESULT: {x:} x {y:} = {product:}")
	if product == x * y:
		print(" | **CORRECT**")
	else:
		print(" | **WRONG**")
		failed_tests += 1
	print(" | \n")

print("============== RESULTS OF ALL TESTS ==============")
print(f"\nTOTAL TESTS RUN: {tests}")
print("\nOVERALL RESULT:\n")
if failed_tests:
	print("\t---------")
	print("\t| FAIL. |")
	print("\t---------")
	print(f"\n\t{failed_tests} were failed.")
else:
	print("\t---------")
	print("\t| PASS! |")
	print("\t---------")
	print(f"\n\tAll {tests} tests were passed! Niceee.")
print("\n==================================================")
