# April 13, 2022

"""
Count the number of inversions in a list.

This implementation uses brute force.
"""

import doctest


def count_inversions(array: list) -> int:
	"""
	Count the number of inversions in an array.

	>>> count_inversions([1, 2, 4, 3])
	1

	>>> count_inversions([1, 5, 3, 2, 4, 6])
	4
	"""

	n = len(array)
	inversions = 0
	for i in range(n):
		for j in range(i + 1, n):
			if array[i] > array[j]:
				inversions += 1
	return inversions

def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()
	myarray = [1, 5, 3, 2, 4, 6]
	myinversions = count_inversions(myarray)
	print(f'Counted {myinversions} inversions in {myarray}.')
	if myinversions == 4:
		print('\t> That\'s correct!')
	else:
		print('\t> That\'s wrong :(')
