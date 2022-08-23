# Learning Algorithms
# Single-Source Shortest Path with Weighted Edges
# Dijkstra's Algorithm
# August 22, 2022

# Stanford Algorithms Specialization
# Class 2 - Week 3 - Programming Assignment

# DESCRIPTION
# Goal:
# The goal of this problem is to implement the "Median Maintenance" algorithm.
# The text file contains a list of the integers from 1 to 10,000 in unsorted
# order; you should treat this as a stream of numbers, arriving one by one.

# Letting xi denote the ith number of the file, the kth median mk is defined
# as the median of the numbers x1, ..., xk. The median of k elements is:
# median = { (k + 1) / 2    if k is odd
#          { k / 2          if k is even

# You should calculate the sum of the 10,000 medians (m1 + m2 + ... + m10_000)
# and provide the last 4 digits of the result (i.e. SUM % 10_000)

# Method:
# Median Maintenance using Two Heaps
# Create two heaps, H_low and H_high, such that all numbers in H_low are less
# than the median value and all numbers in H_high are greater than the median.
# Further, H_low is a max-heap and H_high is a min-heap. Then, at all times,
# the median value is either the max of H_low or the min of H_high.
# As a new number is added to the set, it is placed in the appropriate heap.
# If necessary, rebalancing is done in order to maintain the invariant that
#  the size of each heap is equal to n/2 (+/- 1), where n is the combined size.
# The median of the set of numbers is:
# median = { max of H_low                           if n is even
#          { min of the larger of H_low and H_high  if n is odd

# ============================== IMPLEMENTATION ==============================
from data_structures.heap import Heap


def read_stream(fn):
    """Read integers from txt file into a list"""
    with open(fn) as f:
        lines = list(map(int, f.readlines()))
    return lines


def calculate_medians(stream):
    """Read numbers from stream, maintaining median at each step"""

    h_low = Heap()  # max-heap of all numbers less than or equal to median
    h_high = Heap()  # min-heap of all numbers greater than or equal to median
    size = 0  # combined size of both heaps

    # store median value after each new number is added from stream
    median = 0
    medians = []

    # helper function to add new number to appropriate heap
    def add(num):
        if num <= median:
            h_low.insert(-num)
        else:
            h_high.insert(num)

    # helper function to rebalance heaps
    def rebalance_heaps():
        # Case 1: h_low too big
        if h_low.size - h_high.size > 1:
            extracted = h_low.extract_min()
            h_high.insert(-extracted)
        # Case 2: h_high too big
        elif h_high.size - h_low.size > 1:
            extracted = h_high.extract_min()
            h_low.insert(-extracted)

    # helper function to udpate the median value
    def update_median():
        if size % 2 == 0 or h_low.size > h_high.size:
            return -h_low.get_value(0)
        return h_high.get_value(0)

    # add one number at a time from stream to heaps
    for num in stream:
        add(num)
        size += 1
        rebalance_heaps()
        median = update_median()
        medians.append(median)

    return medians


# =============================== DRIVER CODE =================================

if __name__ == "__main__":
    fn = "median_maintenance_input.txt"
    stream = read_stream("algorithms/input-files/" + fn)
    medians = calculate_medians(stream)
    print('Assignment Answer:', sum(medians) % 10_000)
