#March 29, 2022
"""
Bubble Sort

Bubble sort is a simple algorithm for sorting an unsorted list.
It evaluates adjacent pairs of numbers, and swaps them if they are out of
 order, and moves through each item in this manner until it reaches the end.
It then iterates this process again, each time moving the end point up by
 1 element towards the beginning, until the end is reached, or no more swaps
 are needed.

Think of the larger numbers in the beginning of the list "bubbling" up to
 the end of the list to where they belong.
"""

import time
import random


def bubble_sort(unsorted_list: list) -> list:
    """
    V1 is the most intuitive, by using a nested for loop.

    :param unsorted_list: the list to be sorted
    :return: a sorted copy of the given list
    """
    sorted_list = unsorted_list.copy()
    n = len(sorted_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

def bubble_sort2(unsorted_list: list) -> list:
    """
    V2 adds a boolean to stop the algorithm if no swaps are made on a given pass

    :param unsorted_list: the list to be sorted
    :return: a sorted copy of the given list
    """
    sorted_list = unsorted_list.copy()
    n = len(sorted_list)
    swap_completed = True
    while swap_completed:
        for i in range(n-1):
            swap_completed = False
            for j in range(n-i-1):
                if sorted_list[j] > sorted_list[j+1]:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                    swap_completed = True
    return sorted_list


if __name__ == '__main__':
    # TEST CASES
    lst = [random.randint(0, 100) for _ in range(20)]

    print('---Test Case 1---')
    start1 = time.perf_counter()
    result = bubble_sort(lst)
    end1 = time.perf_counter()
    print('\tUnsorted List:', lst)
    print('\tV1: Sorted List:', result)
    if result == sorted(lst):
        print('\tV1: Assertion Statement Passed!')
    else:
        print('\tV1: Assertion Statement FAILED')
    time1 = end1 - start1

    print('---Test Case 2---')
    start2 = time.perf_counter()
    result = bubble_sort(lst)
    end2 = time.perf_counter()
    print('\tUnsorted List:', lst)
    print('\tV1: Sorted List:', result)
    if result == sorted(lst):
        print('\tV1: Assertion Statement Passed!')
    else:
        print('\tV1: Assertion Statement FAILED')
    time2 = end2 - start2

    print('\n\tAnalysis of Execution Times for Each Version:')
    print('\tV1 Execution Time:', time1)
    print('\tV2 Execution Time:', time2)
    print('\tV2 Faster?', time2<time1)
