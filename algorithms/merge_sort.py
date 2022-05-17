# April 6, 2022

"""
Merge Sort

A divide-and-conquer sorting algorithm implemented recursively.

Merge sort is more efficient than quadratic-time sorting algorithms, such as
 SelectionSort, InsertionSort, and BubbleSort.

Split the array into two parts, then sort each part recursively.
Merge the two sorted parts into the final sorted list.

Base Case: len(array) <= 1 --> Return array

Note: I added doctests (in addition to my own custom tests) as I was
experimenting with the doctest library.
"""
# DO NOT CHANGE debug HERE. SEE BELOW.
debug = False  # Set to false for any external imports / calls


def merge(a: list, b: list, layer=0) -> list:
    """
    The merge subroutine of the merge_sort algorithm.
    Merge two sorted lists into a single sorted list.

    >>> merge([0, 1, 5], [-5, 2, 4])
    [-5, 0, 1, 2, 4, 5]
    """
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # Either a or b will have at least 1 remaining element
    c += a[i:]
    c += b[j:]
    if debug: print(f"{' '*layer*4}>> Merged Result: {c}")
    return c


def merge_sort(lst: list, layer=0) -> list:
    """
    Sort a list using the merge sort algorithm

    >>> merge_sort([12, -5, 0, 99, 4, 12, -1, 32])
    [-5, -1, 0, 4, 12, 12, 32, 99]
    """
    layer += 1
    mid = int(len(lst) // 2)
    if debug: print(f"{' '*layer*4}New Layer for {lst}...")
    if len(lst) <= 1:
        if debug: print(f"{' '*layer*4}> Base: return self")
        return lst
    else:
        a = lst[:mid]
        b = lst[mid:]
        if debug: print(f"{' '*layer*4}a: {a}, b: {b}...")
        return merge(merge_sort(a, layer), merge_sort(b, layer), layer)


# ================================ TEST CASES ================================

if __name__ == '__main__':

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements from function execution
    debug = True
    # ------------------------------------------------------------------------

    import doctest
    temp = debug
    debug = False
    doctest.testmod()

    tests = 0
    failed_tests = 0
    divider_width = 60

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_list = [5, 4, 9, 1, 8, 7]
    print('Unsorted List:', test_list)
    sorted_list = merge_sort(test_list)
    print('Sorted List:', sorted_list)

    if sorted_list == sorted(test_list):
        print("\n > Result: **CORRECT**\n")
    else:
        print("\n > Result: **WRONG**\n")
        failed_tests += 1

    print(f" TEST CASE: Add Negatives and Zero ".center(divider_width, "-"))
    tests += 1
    test_list = [5, 4, -9, -1, 8, 7, 0, -12]
    print('Unsorted List:', test_list)
    sorted_list = merge_sort(test_list)
    print('Sorted List:', sorted_list)

    if sorted_list == sorted(test_list):
        print("\n > Result: **CORRECT**\n")
    else:
        print("\n > Result: **WRONG**\n")
        failed_tests += 1

    print(f" TEST CASE: Add Duplicates ".center(divider_width, "-"))
    tests += 1
    test_list = [5, 4, -9, -1, 8, 7, 0, 4, 9]
    print('Unsorted List:', test_list)
    sorted_list = merge_sort(test_list)
    print('Sorted List:', sorted_list)

    if sorted_list == sorted(test_list):
        print("\n > Result: **CORRECT**\n")
    else:
        print("\n > Result: **WRONG**\n")
        failed_tests += 1

    print(f" ALL RESULTS ".center(divider_width, "="))
    print(f"\nTOTAL TESTS RUN: {tests}")
    print("\nOVERALL RESULT:\n")
    if failed_tests:
        print(f"\t{failed_tests} test(s) failed.\n")
        print("\t===========")
        print("\t|| FAIL. ||")
        print("\t===========")
    else:
        print(f"\tAll {tests} tests passed! Niceee.\n")
        print("\t===========")
        print("\t|| PASS! ||")
        print("\t===========")
    print("".center(divider_width, '='))
