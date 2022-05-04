# Leetcode Problem #53
# Maximum Subarray
# Andrew Tracey
# May 4, 2022

# CATEGORY
# Arrays and Dynamic Programming

# PROBLEM DESCRIPTION
# Given an integer array nums, find the contiguous subarray (containing 
# at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(nums):
    """Dynamic programming - bottom-up solution"""

    # Each subarray ends at a particular index. So, if we find the max
    # subarray ending at each index, then we can return the max of those
    # max values.
    # We'll save the max values in a parallel array, and set the initial
    # max value for each element to its own value (since)
    max_sums = nums.copy()

    # Subproblem: the max_sum for a particular index is equal to its value
    # plus the max_sum for the previous element, IF that max_sum is positive,
    # because only in that case would it increase the max_sum of the current.
    # Therefore, we must start from the left side of the array and calculate
    # the max_sum ending at each element.
    for i in range(1, len(nums)):
        if max_sums[i-1] > 0:
            max_sums[i] = nums[i] + max_sums[i-1]

    # Return the max value from max_sums
    return max(max_sums)


# Driver Code
if __name__ == '__main__':

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# Test Function Decorator ----------------------------------------------------

    def test_decorator(func):
        """Decorator function to wrap around the solution"""
        def wrapper(expected, description, *args, **kwargs):
            """Wrapper function around function passed to decorator"""
            global tests, failed_tests, divider_width
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            tests += 1
            print('Input:', *args, **kwargs)
            result = func(*args, **kwargs)
            print('Output:', result)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_result}\n")
                failed_tests += 1

        return wrapper

    solution = test_decorator(solution)

# TEST CASES -----------------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = [[-2,1,-3,4,-1,2,1,-5,4]]
    kwargs = {}
    expected_result = 6
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[1]]
    kwargs = {}
    expected_result = 1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = [[5,4,-1,7,8]]
    kwargs = {}
    expected_result = 23
    solution(expected_result, test_case_description, *args, **kwargs)
    

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
