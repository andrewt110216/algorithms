# Andrew Tracey
# 3/23/22
# Topic: Recursive Solution to Karatsuba Integer Multiplication

# Worked on this after the example was presented as an algorithm in the
#  intro for the Stanford Algorithms course on Coursera.

# This is an improved version of my first attempt, which wasn't technically
#  Karatsuba (4 recursive calls instead of 3) and only worked for integers with
#  up to 15 digits...not great!


from random import randrange


debug = False  # Keep False here for external imports. Change below.

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

	if debug: print(f" |{' '*layer*4}Starting Karatsuba for {x} and {y}...")
	layer += 1

	# Base Case: If n = 1, then use basic operation of single digit mult.
	if len(str(x)) == 1 and len(str(y)) == 1:
		if debug: print(f" |{' '*layer*4}> Result: {x * y:,}")
		return x * y
	# Otherwise, recurisvely use Karatsuba Algorithm
	else:
		n = max(len(str(x)), len(str(y))) // 2
		# Split x and y into two smaller numbers
		a = x // 10**n
		b = x % 10**n
		c = y // 10**n
		d = y % 10**n
		if debug: print(f" |{' '*layer*4}\ta-b-c-d =", 
			str(a) + "-" + str(b) + "-" + str(c) + "-" + str(d))

		# Call Karatsuba to calculate the smaller products required
		ac = karatsuba(a, c, layer)
		bd = karatsuba(b, d, layer)
		ad_plus_bc = karatsuba(a+b, c+d, layer) - ac - bd

		# Using 2 * length // 2 takes car of even and odd lengths
		prod = ac * 10**(2*n) + (ad_plus_bc * 10**n) + bd
		
		if debug: print(f" |{' '*layer*4}> Result: {int(prod):,}")
		return prod


if __name__ == "__main__":
	# -------------------------------- TEST CASES --------------------------------

	# ============================================================================
	# Set to true to see debugging print statements from function execution
	debug = True
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


	n = 65  # ONLY WORKS WITH N UP TO 15...not sure why :( 
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
