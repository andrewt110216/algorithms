# Learning Algorithms
# Quick Sort - Count Total Number of Comparisons
# Andrew Tracey
# April 27, 2022

# Stanford Algorithms Specialization
# Class 1 - Week 3 - Programming Assignment

# DESCRIPTION
# Given a text file containing all the integers between 1 and 10,000
# (inclusive) in unsorted order, compute the total number of comparisons used
# to sort the given input file by QuickSort. As this depends on the chosen
# pivot, you will explore three different pivoting rules.

# SEE DRIVER CODE BELOW TEST CASES FOR 3 SEPARATE PIVOT RULES

# ============================== IMPLEMENTATION ==============================

def get_pivot_index(choose_method, arr, begin, end):
    """
    Return the index of the pivot element using the provided method

    :param str choose_method: identify the method to use to choose the pivot
    :param list arr: the entire input array
    :param int begin: the index of the beginning of the relevant subarray
    :param int end: the index of the end of the relevant subarray
    :return int: the index (of the entire array) of the chosen pivot element
    """

    if choose_method == 'first':
        return begin
    elif choose_method == 'last':
        return end
    elif choose_method == 'median-of-three':
        mid = (end + begin) // 2
        # A bit of a cheat...need to code up a better way to find the median
        mid_value = sorted([arr[begin], arr[mid], arr[end]])[1]
        if mid_value == arr[begin]:
            return begin
        elif mid_value == arr[mid]:
            return mid
        elif mid_value == arr[end]:
            return end
    else:
        return begin

def partition(arr, start, end, pivot_index):
    """
    Partition the subsection of arr between start and end (inclusive) around
    a pivot element.

    :param list arr: the entire list
    :param int start: the index of the first element of the subarray
    :param int end: the index of the last element of the subarray
    :param int pivot_index: the index of the chosen pivot
    :side effect: sort the input array that was passed by reference
    """

    pivot = arr[pivot_index]
    # Swap the pivot element into the first position
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    i = start + 1  # the first evaluated number that is greater than pivot
    if debug:
        print(f' > Start Partition on {arr[start:end]}. P={pivot}. arr={arr}.')

    for j in range(start + 1, end + 1):
            if debug: print(f'   > Scanning...i={i}, j={j}')
            if arr[j] < pivot: # if arr[j] > pivot => do nothing
                # Swap arr[j] and arr[i] and increment i
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

    # With j exhausted, final step is to swap pivot (arr[start]) with arr[i-1]
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    if debug:
        print(f' > End Partition on {arr[start:end]}. P_i={i-1}. arr={arr}.')

    # Add the number of comparisons to the global comps list
    global comparisons
    len_subarr = end - start + 1
    comparisons.append(len_subarr - 1)

    # Return the index of the partition
    return i - 1

def quick_sort(arr, l, r, pivot_method='first', layer=0):
    """
    Implement QuickSort algorithm to sort an array in place.

    :param list arr: the array
    :param int l: the index of the first element of the subarray
    :param int r: the index of the last element of the subarray
    :param str pivot_method: the method to be used to choose the pivot
    :param int layer: counts the # of recursive calls for debugging
    :side effect: sort the input array that was passed by reference
    """

    layer += 1
    if debug: print(f'Starting layer {layer}. l={l}, r={r}.')
    n = r - l + 1
    if n == 1:
        return # No sorting needed
    if l < r:
        pivot_index = get_pivot_index(pivot_method, arr, l, r)
        k = partition(arr, l, r, pivot_index)
        quick_sort(arr, l, k - 1, pivot_method, layer)
        quick_sort(arr, k + 1, r, pivot_method, layer)

def get_input(path):
    """Read the integer found on each line of the text file into a list"""
    with open(path) as f:
        contents = f.readlines()
    output_array = []
    for line in contents:
        output_array.append(int(line.strip()))
    return output_array

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
    comparisons = []
    quick_sort(working_array, 0, length-1, pivot_method='last')
    print('Output:', working_array)
    print('Comparisons:', sum(comparisons))

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
    comparisons = []
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)
    print('Comparisons:', sum(comparisons))

    expected_result = 0
    if sum(comparisons) == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 2".center(divider_width, "-"))
    tests += 1
    test_input = [3, 5]
    length = len(test_input)
    working_array = test_input.copy()
    print('Input:', test_input)
    comparisons = []
    quick_sort(working_array, 0, length-1)
    print('Output:', working_array)
    print('Comparisons:', sum(comparisons))

    expected_result = 1
    if sum(comparisons) == expected_result:
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

# DRIVER CODE FOR ASSIGNMENT SOLUTIONS
# ===========================================================================
filepath = 'algorithms/input-files/quick_sort_input.txt'
input_array = get_input(filepath)
length = len(input_array)

# 1. Pivot is the first element of the array
print('\n*** PROGRAMMING ASSIGNMENT - PART 1 - First Element ***')
working_array = input_array.copy()
comparisons = []
quick_sort(working_array, 0, length - 1, pivot_method='first')
print(' Total Comparisons:', f'{sum(comparisons)}')  # 162,085

# 2. Pivot is the last element of the array
print('\n*** PROGRAMMING ASSIGNMENT - PART 2 - Last Element ***')
working_array = input_array.copy()
comparisons = []
quick_sort(working_array, 0, length - 1, pivot_method='last')
print(' Total Comparisons:', f'{sum(comparisons)}')  # 164,123

# 3. Use the median-of-three method
print('\n*** PROGRAMMING ASSIGNMENT - PART 3 - Median-of-Three ***')
working_array = input_array.copy()
comparisons = []
quick_sort(working_array, 0, length - 1, pivot_method='median-of-three')
print(' Total Comparisons:', f'{sum(comparisons)}')  # 138,382
