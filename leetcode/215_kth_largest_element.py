# Leetcode Problem #215
# Kth Largest Element in an Array

# PROBLEM DESCRIPTION
# Given an integer array nums and an integer k, return the kth largest
# element in the array
# Note that it is the kth largest element in the sorted order, not the
# kth distinct element.

# Example:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
# 
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k=4
# Output: 4

# PLAN:
# Use a modified version of QuickSort.
# Search for the (n-k)th index element in ascending order.
# Base Case: n = 1: return nums[n]
# Choose Pivot randomly
# Partition nums around pivot, resulting in pivot at position p.
# If k = p, return nums[p]
# If k < p, recurse on left side
# If k > p, recurse on right side

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

class Solution:
    def findKthLargest(self, nums, k):
        """Return the k-th largest element of nums"""

        # Convert from k-th largest to i-th smallest
        i = len(nums) - k

        def partition(arr, pivot_index):
            pivot = arr[pivot_index]
            arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
            i = 1
            for j in range(1, len(arr)):
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            arr[0], arr[i - 1] = arr[i - 1], arr[0]
            return i - 1

        def recurse(nums, target_index):
            n = len(nums)
            if n == 1:
                return nums[0]
            else:
                import random
                pivot_index = random.randint(0, n-1)
                partition_index = partition(nums, pivot_index)
                if partition_index == target_index:
                    return nums[partition_index]
                elif target_index < partition_index:
                    return recurse(nums[:partition_index], target_index)
                elif target_index > partition_index:
                    target_index = target_index - partition_index - 1
                    return recurse(nums[partition_index+1:], target_index)

        return recurse(nums, i)

# ================================ TEST CASES ================================

if __name__ == '__main__':

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = True
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_array = [3, 2, 1, 5, 6, 4]
    test_k = 2
    print('Input:', test_array, 'k:', test_k)
    sol = Solution()
    result = sol.findKthLargest(test_array, test_k)
    print('Output:', result)

    expected_result = 5
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Length 1 ".center(divider_width, "-"))
    tests += 1
    test_array = [5]
    test_k = 1
    print('Input:', test_array, 'k:', test_k)
    sol = Solution()
    result = sol.findKthLargest(test_array, test_k)
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
    test_array = [5, 4]
    test_k = 2
    print('Input:', test_array, 'k:', test_k)
    sol = Solution()
    result = sol.findKthLargest(test_array, test_k)
    print('Output:', result)

    expected_result = 4
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Negs, 0's, Duplicates ".center(divider_width, "-"))
    tests += 1
    test_array = [-7, 9, -5, 0, 3, 9, -5, -1, 10, 8, 6, -1]
    test_k = 9
    print('Input:', test_array, 'k:', test_k)
    sol = Solution()
    result = sol.findKthLargest(test_array, test_k)
    print('Output:', result)

    expected_result = -1
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
