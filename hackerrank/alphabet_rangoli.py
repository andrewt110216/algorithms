# Hackerrank Problem
# Alphabet Rangoli

# --- PROBLEM DESCRIPTION ---
# You are given an integer, N.
# Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

# Example: size N=3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string


def print_rangoli(size):
	"""print rangoli for the given size"""

	# create list of letters, replacing letters outside range with '-'
	alpha = list(string.ascii_lowercase)
	for i in range(len(alpha)):
		if i > size - 1:
			alpha[i] = '-'

	rangoli_str = ''
	rangoli_lst = []
	for i in range(size):
		# assemble the letters for the line of rangoli in a list
		line_lst = []
		for j in range(size):
			try:
				line_lst.append(alpha[i + j])
			except IndexError:
				line_lst.append('-')
		line_lst = line_lst[-1:0:-1] + line_lst[:]
		# join together the list of letters into a string, with dashes
		line_str = '-'.join(line_lst)
		# add string to list of lines, called rangoli_lst
		rangoli_lst.append(line_str)

	# you have created the bottom half of the rangoli.
	# now, create top half by copying and flipping the bottom half
	rangoli_lst = rangoli_lst[-1:0:-1] + rangoli_lst[:]
	# join the lines of rangoli_lst into a string, adding '\n'
	for line in rangoli_lst:
		rangoli_str += line + '\n'
	# remove '\n' from the final row
	rangoli_str = rangoli_str.strip()
	print(rangoli_str)


# *** TEST CASES ***
print('---TEST CASE 1: N = 3 ---')
print_rangoli(3)

print('---TEST CASE 2: N = 9 ---')
print_rangoli(9)

print('---TEST CASE 3: N = 26 ---')
print_rangoli(26)
