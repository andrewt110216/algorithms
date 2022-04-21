# Learning Algorithms
# Count Inversions (Divide & Conquer)
# Andrew Tracey
# April 20, 2022

# DESCRIPTION
# Goal:
# Count the number of inversions in a given array of length n, with the
# distinct elements 1 to n, where an inversion is every pair of indexes i, j
# where i < j and arr[j] < arr[i]. That is, arr[j] is to the right of arr[i]
# and is a smaller value than it.

# Method:
# Piggyback on the merge sort algorithm, taking advantage of the fact that in
# the merge subroutine of that algorithm, any time we copy an item from the
# right array into our merged array this represents a number of inversions
# equal to the remaining elements in the left array.

# Notes:
# Since we are piggybacking on merge sort, which we know runs in n*logn time,
# and we are only adding the addition of the accumulation, our algorithm also
# runs in O(n*logn) time.
# This is an accomplishment, since we know that the brute force iterative
# approach is O(n). See separate file for the iterative algorithm.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================


def merge(a, b):
    """Merge two sorted lists and count the split inversions"""

    c = []
    i, j = 0, 0
    count = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            count += len(a) - i

    # Clean up remainder
    c += a[i:]
    c += b[j:]

    return c, count


def sort_and_count(array):
    """Sort an array and count the number of inversions"""

    # Base Case
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left_sorted, x = sort_and_count(left)
    right_sorted, y = sort_and_count(right)
    merged, z = merge(left_sorted, right_sorted)
    total_inversions = x + y + z

    return merged, total_inversions


def read_input_from_file(filepath: str) -> list:
    """
    Read the contents of the input file to a list.

    param filepath: path to a txt file containing n distinct integers in the
        range 1 to n, with each integer on a separate line
    """
    with open(filepath) as f:
        contents = f.readlines()
    contents = [int(line.strip()) for line in contents]
    return contents

# ================================ TEST CASES ================================


if __name__ == '__main__':

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements, if any, from execution
    debug = False
    # ------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_input = [1, 2, 4, 3, 6, 5]
    print('Input:', test_input)
    result = sort_and_count(test_input)[1]
    print('Output:', result)

    expected_result = 2
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Larger ".center(divider_width, "-"))
    tests += 1
    test_input = [12, 8, 3, 4, 7, 9, 10, 11, 2, 1, 5, 6]
    print('Input:', test_input)
    result = sort_and_count(test_input)[1]
    print('Output:', result)

    expected_result = 39
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case -------------------------------------------------------------

    print(f" Test: Huge Input".center(divider_width, "-"))
    tests += 1
    test_input = read_input_from_file('count_inversions_input.txt')
    print(f'Input Length {len(test_input):,}')
    print('First 15 elements:', test_input[:15], '...')
    result = sort_and_count(test_input)[1]
    print('Output:', result, '\n')

    expected_result = 2407905288  # Per Coursera Stanford: Algorithms class
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
