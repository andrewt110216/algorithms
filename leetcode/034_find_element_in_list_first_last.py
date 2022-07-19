# Leetcode Problem #34
# Find First and Last Position of Element in Sorted Array

# PROBLEM DESCRIPTION
# Given an array of integers (nums) sorted in non-decreasing order, find the
# first and last position of a given target value.
# If target is not found in nums, return [-1, -1].
# The algorithm must have O(log n) runtime complexity.

# Example 1:
# Input: [5, 7, 7, 8, 8, 10], target = 8
# Output: [3,4]

# Example 2:
# Input: [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: [], target = 0
# Output: [-1,-1]

# PLAN
# Use binary search, which runs in O(log n), as needed.
# When we find a match, we'll need to store it AND its index. In fact, we
# should only store its index, and all indexes at which we find a match.
# Then, we'll simply sort the index locations, and return the first and last.
# Is it too costly to also sort that list? It is, in fact, since sorting in
# Python has time complexity O(n * log n), which is too big...hmm...
# We'll have to be more clever. At each recursive call, we'll have to return
# only the highest and lowest indexes where target is found. It is OK to add
# operations in the recursions, as long as they are independent of n.
# ...OK. I just got it. The array is already sorted! So once we find a match,
# we don't actually have to contine. We just have to look left and right until
# we find a different number, and return the outermost positions of target!

# CONCLUSION
# This implementation turned out to still be a bit tricky. After finding a match, it was
# difficult to manage the indexes of the linear scan left/right to not go out
# of bounds was difficult, and, doing a linear scan actually could increase
# the overall runtime to O(n), if, say, all elements of the array were
# the target.
# PLEASE SEE V2 SOLUTION IN SEPARATE FILE.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
class Solution:
    def searchRange(self, nums, target, start=0, end=None):
        """Find the first and last position of target in nums"""

        # Make sure num is nonempty. If not, return [-1, -1]
        if nums:
            # Initiate the end value
            if end is None:
                end = len(nums)
            # Recursively search for target with binary search
            if end > start:
                mid = (start + end) // 2
                if target == nums[mid]:
                    # Set the first and last occurences to mid
                    first = last = mid
                    # Go left for as long as the value is still target
                    while first > 0 and nums[first - 1] == target:
                        first -= 1
                    # Now go right
                    while last < len(nums) - 1 and nums[last + 1] == target:
                        last += 1
                    return [first, last]
                elif target < nums[mid]:
                    args = [nums, target, start, mid - 1]
                    return self.searchRange(*args)
                elif target > nums[mid]:
                    args = [nums, target, mid + 1, end]
                    return self.searchRange(*args)

        # No matches found
        return [-1, -1]

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
    test_input = ([5, 7, 7, 8, 8, 10], 8)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [3, 4]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: No Match ".center(divider_width, "-"))
    tests += 1
    test_input = ([5, 7, 7, 8, 8, 10], 6)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [-1, -1]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Empty List ".center(divider_width, "-"))
    tests += 1
    test_input = ([], 0)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [-1, -1]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Negatives and Zeros".center(divider_width, "-"))
    tests += 1
    test_input = ([-5, -5, -5, -5, -5, -1, 0, 0, 1, 1, 3, 6, 9, 100], -5)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [0, 4]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Only One Value".center(divider_width, "-"))
    tests += 1
    test_input = ([2, 2], 2)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [0, 1]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Input Size 1".center(divider_width, "-"))
    tests += 1
    test_input = ([1], 1)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [0, 0]
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
