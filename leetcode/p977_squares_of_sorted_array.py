# Leetcode Problem #977
# Squares of a Sorted Array
# Andrew Tracey
# May 3, 2022

# PROBLEM DESCRIPTION
# Given an integer array nums sorted in non-decreasing order, return
# an array of the squares of each number sorted in non-decreasing order

# Example:
# Input: nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

# Notes
# Intution is to compute the squares, and then to sort.
# This would take a runtime of O(n) to compute the squares and then
# O(nlogn) to sort using merge sort.
# Can we do better, by acheiving a runtime of O(n)?
# Possibly by completing the sort at the same time
# as we calculate the squares? The provided hint was that this problem
# could use a two pointer solution.
# Note that our squared array is partitioned around 0, with both sides
# already sorted. So, essentially, we only need to complete the merge
# subroutine one time, with the separated arrays, taking the negative
# numbers in reverse order.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def sortedSquares(nums:list) -> list:
    # V2 implementation. See notes below in V1

    # Set up pointers
    n = len(nums)
    left = 0
    right = n - 1
    result = [0] * n
    
    # Iterate result in reverse, since by incrementing from the ends,
    # we are moving in descending order (in absolute values)
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            x = nums[right]
            right -= 1
        else:
            x = nums[left]
            left += 1
        result[i] = x * x

    return result

def sortedSquaresV1(nums:list) -> list:
    # V1 Implementation took the unnecessary step of iterating to find
    # the first non-negative element.
    # In the above version, we will simply start from the left and right
    # ends of the array, and consider only the absolute values
    
    # Find the 'pivot' element: the first non-negative num
    p = 0
    while p < len(nums):
        if nums[p] >= 0:
            break
        p += 1
    # If p is 0, there are no negative nums, making the task trivial
    if p == 0:
        return [x**2 for x in nums]
    # Now, merge the negative nums (sorted in non-increasing order),
    # and the non-negative nums (sorted in non-decreasing order)
    
    # Set up pointers
    neg_pointer = p - 1
    non_neg_pointer = p
    result = []
    
    # Iterate through subarrays, merging into result
    while neg_pointer >= 0 and non_neg_pointer < len(nums):
        if -nums[neg_pointer] < nums[non_neg_pointer]:
            result.append(nums[neg_pointer]**2)
            neg_pointer -= 1
        else:
            result.append(nums[non_neg_pointer]**2)
            non_neg_pointer += 1
    
    # Clean up remaining elements in either subarray
    while neg_pointer >= 0:
        result.append(nums[neg_pointer]**2)
        neg_pointer -= 1
    while non_neg_pointer < len(nums):
        result.append(nums[non_neg_pointer]**2)
        non_neg_pointer += 1
    
    return result

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
    test_input = [-4, -1, 0, 3, 10]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: No Negatives ".center(divider_width, "-"))
    tests += 1
    test_input = [1, 3, 7, 10, 12, 15]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: No Non-Negatives ".center(divider_width, "-"))
    tests += 1
    test_input = [-8, -5, -4, -2, -1]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Single Element: Pos ".center(divider_width, "-"))
    tests += 1
    test_input = [3]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Single Element: Neg ".center(divider_width, "-"))
    tests += 1
    test_input = [-3]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1


# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Two Element ".center(divider_width, "-"))
    tests += 1
    test_input = [-1, 5]
    print('Input:', test_input)
    result = sortedSquares(test_input)
    print('Output:', result)

    expected_result = sorted([x**2 for x in test_input])
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
