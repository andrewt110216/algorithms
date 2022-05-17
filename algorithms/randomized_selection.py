# Learning Algorithms
# Randomized Selection
# Andrew Tracey
# April 28, 2022

# DESCRIPTION
# Goal: find the ith smallest number in an array of n distinct elements
# Method:
# Use a modified version of the QuickSort algorithm.
# After the first partition, determine if the ith element is in the left
# or right half, and then only recurse on that subarray. Continue until
# either the ith element happens to be chosen as the pivot, or until the
# base case of array length 1.
# Use randomization to choose the pivot element in each partition call.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================
import random


def Partition(arr, pivot_index):
    """Partition arr around arr[pivot_index]"""

    # Save the pivot element value, and swap it into the first position
    n = len(arr)
    pivot = arr[pivot_index]
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    if debug: print(f'   > Start Partition on {arr}. P={pivot}')
    i = 1
    for j in range(1, n):
        if debug: print(f'     > Scanning...i={i}, j={j}')
        if arr[j] < pivot:
            # Swap arr[j] and arr[i] and increment i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # With j exhausted, final step is to swap pivot with arr[i-1]
    arr[0], arr[i - 1] = arr[i - 1], arr[0]
    if debug: print(f'   > End Partition on {arr}. pivot_index={i-1}. ')
    return i - 1

def RSelect(arr, n, i):
    """Return the ith order item of the list arr with n distinct items"""
    if n == 1:
        return arr[0]
    else:
        pivot_index = random.choice(range(n))
        if debug: print(f'Call Partition(arr={arr}, pivot={arr[pivot_index]})')
        j = Partition(arr, pivot_index)
        if j == i:
            return arr[j]
        elif i < j:
            if debug: print(f' > Call RSelect(arr={arr[0:j]}, len={j}, selection={i})')
            j = RSelect(arr[0:j], j, i)
            if debug: print(f' > Returning {j}')
            return j
        elif i > j:
            if debug: print(f' > Call RSelect(arr={arr[j+1:]}, len={n-j-1}, selection={i-j-1})')
            j = RSelect(arr[j+1:], n-j-1, i-j-1)
            if debug: print(f' > Returning {j}')
            return j

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
    test_input = [2, 7, 1, 4, 0, 3, 6, 5]
    selection_element = 4
    print('Input Array:', test_input)
    print('Selection Element:', selection_element)
    n = len(test_input)
    working_array = test_input.copy()
    result = RSelect(working_array, n, selection_element)
    print('Output:', result)

    expected_result = 4
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 1 ".center(divider_width, "-"))
    tests += 1
    test_input = [5]
    selection_element = 0
    print('Input Array:', test_input)
    print('Selection Element:', selection_element)
    n = len(test_input)
    working_array = test_input.copy()
    result = RSelect(working_array, n, selection_element)
    print('Output:', result)

    expected_result = 5
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 2 ".center(divider_width, "-"))
    tests += 1
    test_input = [4, 2]
    selection_element = 1
    print('Input Array:', test_input)
    print('Selection Element:', selection_element)
    n = len(test_input)
    working_array = test_input.copy()
    result = RSelect(working_array, n, selection_element)
    print('Output:', result)

    expected_result = 4
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Negatives, 0's ".center(divider_width, "-"))
    tests += 1
    test_input = [6, -5, 12, 0, -1, 3, 4, 2, 8, -10, 11]
    selection_element = 7
    print('Input Array:', test_input)
    print('Selection Element:', selection_element)
    n = len(test_input)
    working_array = test_input.copy()
    result = RSelect(working_array, n, selection_element)
    print('Output:', result)

    expected_result = 6
    if result == expected_result:
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
