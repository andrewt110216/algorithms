# Leetcode Problem #34
# Find First and Last Position of Element in Sorted Array
# SOLUTION VERSION #2 - See Version #1 in Separate File

# PROBLEM DESCRIPTION
# Given an array of integers (nums) sorted in non-decreasing order, find the
# first and last position of a given target value.
# If target is not found in nums, return [-1, -1].
# The algorithm must have O(log n) runtime complexity.

# Example 1:
# Input: [5, 7, 7, 8, 8, 10], target = 8
# Output: [3,4]

# PLAN
# We can basically run two binary searches. First, we will do a binary search
# to identify the first occurence of target. Then, we will do another search
# to identify the last occurence. The searches will be done consecutively.
# We will just tweak the binary search alogirthm to allow for the option to
# look for the first or last occurence.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
class Solution:
    def searchRange(self, nums, target, start=0, end=None):
        """Find the first and last position of target in nums"""

        first_position = self.find_bound(nums, target, first=True)
        if first_position == -1:
            return [-1, -1]
        last_position = self.find_bound(nums, target, first=False)

        return [first_position, last_position]

    def find_bound(self, nums, target, first=True):
        """
        Binary search an array for a target value, where the target may
        occur x >= 0 times in array. Return the index of either the first
        or last occurence of target in the array.

        :param list nums: list to be searched
        :param int target: value to be searched for in nums
        :param int start: index at which to start the search
        :param int end: index at which to end the search
        :param boolean first: True to find first occurence; False to find last
        :return int: the index at which target was found; -1 if not found
        """

        # Return -1 if nums is empty
        if not nums:
            return -1

        # Initiate start and end indexes
        n = len(nums)
        start, end = 0, n
        mid = (start + end) // 2

        # Binary search until start >= end
        while start <= end and mid in range(n):
            if target == nums[mid]:
                if first:
                    # Two cases to determine if our value is the first
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    else:  # Ours was not the first
                        end = mid - 1
                else:  # first = False
                    # Two cases to determine if our value is the last
                    if mid in [end, n - 1] or nums[mid + 1] > target:
                        return mid
                    else:  # Ours was not the last
                        start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            # Reset mid for next iteration
            mid = (start + end) // 2

        # No matches found
        return -1

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

    print(f" TEST CASE: Many Targets at Start".center(divider_width, "-"))
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

    print(f" TEST CASE: Many Targets at End".center(divider_width, "-"))
    tests += 1
    test_input = ([0, 0, 1, 1, 3, 6, 9, 100, 112, 112, 112, 112], 112)
    print('Input:', test_input)
    solution = Solution()
    result = solution.searchRange(*test_input)
    print('Output:', result)

    expected_result = [8, 11]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Only One Value (Length 2)".center(divider_width, "-"))
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

    print(f" TEST CASE: Only One Value (Length 2)".center(divider_width, "-"))
    tests += 1
    test_input = ([2, 2], 3)
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

    print(f" TEST CASE: Only One Value (Length 5)".center(divider_width, "-"))
    tests += 1
    test_input = ([6, 6, 6, 6, 6], 6)
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
