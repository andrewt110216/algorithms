# April 6, 2022

"""Compare runtime for different sorting alogorithms"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np

import merge_sort
import insertion_sort
import bubble_sort


def compare_sorting_algorithms(array: list) -> list:
	"""Compare runtimes for different sorting algorithms"""
	algorithms = [
		bubble_sort.bubble_sort2,
		insertion_sort.insertion_sort_v3,
		merge_sort.merge_sort]
	
	runtimes = []
	for algorithm in algorithms:
		start = time.perf_counter()
		algorithm(array)
		end = time.perf_counter()
		runtimes.append(end - start)

	return list(zip(algorithms, runtimes))

# Run the comparisons for varying input quantities

x_values = list(map(int, np.linspace(10, 1_000, 100)))
[10**i for i in range(1, 6)]  # Number of inputs
times_bubble = []
times_insertion = []
times_merge = []

for x in x_values:
	test_list = [random.randrange(x**2) for _ in range(x)]
	run_results = compare_sorting_algorithms(test_list)
	times = list(zip(*run_results))[1]
	times_bubble.append(times[0])
	times_insertion.append(times[1])
	times_merge.append(times[2])

# Visualize to compare
fig, ax = plt.subplots()
ax.plot(
	x_values, times_bubble, 'bo',
	x_values, times_insertion, 'r--',
	x_values, times_merge, '-',)
plt.legend(['Bubble Sort', 'Insertion Sort', 'Merge Sort'])
plt.title('Compare Sorting Algorithm Runtimes for Varying Array Sizes')
plt.xlabel('Length of Array to be Sorted')
plt.ylabel('Runtime of Sorting Algorithm (Seconds)')
ax.set_facecolor('#FCF3CF')
fig.patch.set_facecolor('#D6EAF8')
plt.annotate('Algorithm Implementations by: Andrew Tracey. 2022.',
	(0, 0), (-50, -30), xycoords='axes fraction',
	textcoords='offset points', va='top')
fig.set_size_inches(16, 8)

plt.savefig("comparison_sorting.png")
plt.show()
