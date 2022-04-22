# Learning Algorithms
# Quick Sort
# Andrew Tracey
# April 21, 2022

# DESCRIPTION
# Goal: Sort an array of n distinct elements.
# Method:
# Divide and Conquer.
# Choose a 'pivot' element and partition the elements around the pivot such
# that all elements to the left of the pivot are smaller and all elements to
# the right are larger. Accomplish this by scanning through each element, and
# completing swaps to partition properly.
# Then, recursively sort the subarrays to the left and right of pivot, until
# the entire input array has been sorted.

# NOTES
# Runtime is O(n * log n), because there are logn levels of recursive calls,
# and the Partition subroutine runs in linear time O(n).
# By Master Method, a = 2, b = 2, d = 1 ==> Case 1 ==> T(n) = O(n * log n).

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def partition(arr, start, end):
    """
    Partition the subsection of arr between start and end (inclusive) around
    a pivot element.

    :param list arr: the entire list
    :param int start: the index of the first element of the subarray
    :param int end: the index of the last element of the subarray
    :return: None. Side effect of partitioning the subarray
    """

    pivot = arr[start]
    i = start + 1  # the first evaluated number that is greater than pivot
    if debug:
        print(f' > Start Partition on {arr[start:end]}. P={pivot}. arr={arr}.')

    for j in range(start+1, end+1):
            if debug: print(f'   > Scanning...i={i}, j={j}')
            if arr[j] < pivot: # [if arr[j] > pivot -> do nothing]
                # Swap arr[j] and arr[i] and increment i
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

    # With j exhausted, final step is to swap pivot (arr[start]) with arr[i-1]
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    if debug:
        print(f' > End Partition on {arr[start:end]}. P_i={i-1}. arr={arr}.')
    return i - 1

def quick_sort(arr, l, r, layer=0):
    """
    :param list arr: the array
    :param int l: the index of the first element of the subarray
    :param int r: the index of the last element of the subarray
    :param int layer: counts the # of recursive calls for debugging
    :return: Side effect is sorting the array passed by reference
    """

    layer += 1
    if debug: print(f'Starting layer {layer}. l={l}, r={r}.')
    n = r - l + 1
    if n == 1:
        return  # No sorting needed
    if l < r:
        k = partition(arr, l, r)
        quick_sort(arr, l, k - 1, layer)
        quick_sort(arr, k + 1, r, layer)

# ================================ TEST CASES ================================

if __name__ == '__main__':

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_input = [3, 8, 2, 5, 1, 4, 7, 6]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Neg's & 0, Longer ".center(divider_width, "-"))
    tests += 1
    test_input = [-2, 3, 8, 2, -5, 12, 5, 1, 4, -7, 6, 0, 15]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Empty ".center(divider_width, "-"))
    tests += 1
    test_input = []
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 1 ".center(divider_width, "-"))
    tests += 1
    test_input = [5]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 2 ".center(divider_width, "-"))
    tests += 1
    test_input = [5, 3]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 2, Sorted ".center(divider_width, "-"))
    tests += 1
    test_input = [3, 5]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 3 ".center(divider_width, "-"))
    tests += 1
    test_input = [3, 5, 1]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)

    expected_result = sorted(test_input)
    if working_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# SUMMARY ====================================================================

    print(f" ALL RESULTS ".center(divider_width, "="))
    print(f"\nTOTAL TESTS RUN: {tests}")
    print("\nOVERALL RESULT:\n")
    if failed_tests:
        print(f"\t{failed_tests} test(s) failed.\n")
        print("\t===========")
        print("\t|| FAIL. ||")
        print("\t===========")
    else:
        print(f"\tAll tests passed! Niceee.\n")
        print("\t===========")
        print("\t|| PASS! ||")
        print("\t===========")
    print("".center(divider_width, '='))
