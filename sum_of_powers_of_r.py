# Sum of consecutive powers of a constant

# Basic Fact:
# For constant r > 0 and != 1, and power k >= 0:
# 1 + r + r^2 + ... + r^k = r^(k+1) - 1
#                          _____________
#                              r - 1

# Further, if r > 1, then the sum is upper-bounded by r times a constant
# factor, with that factor being 1 +    1
#                                    _______
# 									  r - 1

def sum_of_powers(r, k):
	"""Calculate the sum of all powers of r ranging from 0 to k"""
	result = 0
	if k < 0:  # k must be positive
		return False
	for n in range(k+1):
		result += r**n
	return result

if __name__ == "__main__":

	import math

	# Test Case 1
	constant = 2
	power = 5
	upper_bound_ratio = round(1 + (1 / (constant-1)),2)
	my_sum = sum_of_powers(constant, power)
	print(f"Sum of powers of {constant} ranging from 0 to {power} = {my_sum:,}")
	print(f"  > The last term of the expression being {constant**power:,}" +\
		f" x {upper_bound_ratio} = {constant**power*upper_bound_ratio:,}")

	# Test Case 2
	constant = 3
	power = 12
	upper_bound_ratio = round(1 + (1 / (constant-1)),2)
	my_sum = sum_of_powers(constant, power)
	print(f"Sum of powers of {constant} ranging from 0 to {power} = {my_sum:,}")
	print(f"  > The last term of the expression being {constant**power:,}" +\
		f" x {upper_bound_ratio} = {constant**power*upper_bound_ratio:,}")

	# Test Case 3
	constant = 5
	power = 20
	upper_bound_ratio = round(1 + (1 / (constant-1)),2)
	my_sum = sum_of_powers(constant, power)
	print(f"Sum of powers of {constant} ranging from 0 to {power} = {my_sum:,}")
	print(f"  > The last term of the expression being {constant**power:,}" +\
		f" x {upper_bound_ratio} = {constant**power*upper_bound_ratio:,}")

