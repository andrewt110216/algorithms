# Learning Algorithms
# Count Inversions (Divide & Conquer)
# Andrew Tracey
# April 20, 2022

# DESCRIPTION
# Goal: Count the number of inversions in a given array of length n, with the
# distinct elements 1 to n, where an inversion is every pair of indexes i, j
# where i < j and arr[j] < arr[i]. That is, arr[j] is to the right of arr[i]
# and is a smaller value than it.
# Method:
# 
# 
# 
# Notes:
# Since we are piggybacking on merge sort, which we know runs in n*logn time,
# and we are only adding the addition of the accumulation, our algorithm also
# runs in O(n*logn) time.
# This is an accomplishment, since we can be counting up to a quadratic number
# of inversions. The case of an array in reverse (descending) order

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def algorithm(i):
	"""DOC STRING"""
	return i

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
    test_input = True
    print('Input:', test_input)
    result = algorithm(test_input)
    print('Output:', result)

    expected_result = True
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

