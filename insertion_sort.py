# January 29, 2022

"""
Insertion Sort

Insertion sort is a basic, brute force sorting algorithm. It is a slight
 improvement on SelectionSort.
 
Essentially, you start with the item at index 1 in the list and compare it to
 the item on it's left. If it is less than that item, then you swap the two
 items. You would keep comparing and swapping with the item to the left until
 the item on the left is smaller than the working item. This way, each item is
 left in it's appropriate spot, and you move all the way through the list in
 this way until the last item.

Another way to describe it would be to sort the list one sub-list at a 
 time, starting with the first two elements. Then, add a new item from the 
 original list onto the end of the sorted sub-list and sort it into place.
Continue adding elements to the sub-list and sorting until you reach the end.
"""

import time


def insertion_sort_v1(unsorted_list: list) -> list:
    """
    V1 is the most intuitive, by using a nested for loop.

    :param unsorted_list: the list to be sorted
    :return: a sorted copy of the given list

    Loop through each index position in the list and compare it to each item
     to its left. If it is less than the item on the left, swap the two
     items; otherwise, it is in position; break the loop and move on.
    """
    sorted_list = unsorted_list.copy()

    for i in range(1, len(sorted_list)):
        for j in range(i - 1, -1, -1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    return sorted_list


def insertion_sort_v2(unsorted_list: list) -> list:
    """
    V2 uses a while loop and makes the item swap in one line, eliminating
     the need to use a temporary variable

    :param unsorted_list: the list to be sorted
    :return: a sorted copy of the given list

    Loop through each index position in the list, then use a while loop to 
     swap with the left-side item until either you get to the beginning of 
     the list or the left-side item is smaller.
    Use the available syntax of swapping the items in a single line, to
     avoid the need to explicitly save a temporary variable.
    """
    sorted_list = unsorted_list.copy()
    for i in range(1, len(sorted_list)):
        while sorted_list[i - 1] > sorted_list[i] and i > 0:
            sorted_list[i - 1], sorted_list[i] = \
                sorted_list[i], sorted_list[i - 1]
            i = i - 1

    return sorted_list


def insertion_sort_v3(unsorted_list: list) -> list:
    """
    V3 uses shifting instead of swapping to optimize speed
    :param unsorted_list: the list to be sorted
    :return: a sorted copy of the given list

    Loop through each index position in the list, save the value at that index
     which is to be sorted, then loop through each item to the left of the
     current index and if it is greater than the current value, then shift it
     to the right; otherwise, this is where the current value belongs so place
     it here.
    """
    sorted_list = unsorted_list.copy()
    for i in range(1, len(sorted_list)):
        value_to_sort = sorted_list[i]
        for j in range(i - 1, -1, -1):
            if sorted_list[j] > value_to_sort:
                sorted_list[j + 1] = sorted_list[j]
                if j == 0:
                    sorted_list[j] = value_to_sort
            else:
                sorted_list[j + 1] = value_to_sort
                break

    return sorted_list


if __name__ == '__main__':
    # TEST CASES
    print('---Test Case 1---')
    lst = [99, 4, 53, 1, 21, 0, 9, 82, 14, 2]
    start_v1 = time.perf_counter()
    result = insertion_sort_v1(lst)
    end_v1 = time.perf_counter()
    print('\tUnsorted List:', lst)
    print('\tV1: Sorted List:', result)
    assert result == [0, 1, 2, 4, 9, 14, 21, 53, 82, 99]
    print('\tV1: Assertion Statement Passed!')

    start_v2 = time.perf_counter()
    result = insertion_sort_v2(lst)
    end_v2 = time.perf_counter()
    print('\tUnsorted List:', lst)
    print('\tV2: Sorted List:', result)
    assert result == [0, 1, 2, 4, 9, 14, 21, 53, 82, 99]
    print('\tV2: Assertion Statement Passed!')

    start_v3 = time.perf_counter()
    result = insertion_sort_v3(lst)
    end_v3 = time.perf_counter()
    print('\tUnsorted List:', lst)
    print('\tV3: Sorted List:', result)
    assert result == [0, 1, 2, 4, 9, 14, 21, 53, 82, 99]
    print('\tV3: Assertion Statement Passed!')

    print('\n\tAnalysis of Execution Times for Each Version:')
    ex_v1 = end_v1 - start_v1
    ex_v2 = end_v2 - start_v2
    ex_v3 = end_v3 - start_v3
    print('\tV1 Execution Time:', ex_v1)
    print('\tV2 Execution Time:', ex_v2)
    print('\tV3 Execution Time:', ex_v3)
