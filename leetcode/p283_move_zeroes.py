# Leetcode Problem #283
# Move Zeroes
# Andrew Tracey
# May 3, 2022

# PROBLEM DESCRIPTION
# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# You MUST complete this in-place, without copying the array

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# length of nums is > 0 and <= 10^4
# each element is positive or negative 2^31

# Follow up:
# Could you minimize the total number of operations done?

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(nums):
    """V2 appropriately uses two actual pointers. See below for V1."""

    # If array is of length 1 or less, no action needed
    n = len(nums)
    if n <= 1:
        return nums

    # Iterate over the list, shifting non-zeroes to the front
    place_next_nonzero = 0
    for current in range(n):
        if nums[current] != 0:
            nums[place_next_nonzero] = nums[current]
            place_next_nonzero += 1

    # Now place 0's at each location after the last nonzero
    for i in range(place_next_nonzero, n):
        nums[i] = 0

    return nums

def solution1(nums):
    """
    First try. Success! My thinking resulted in a sort of backwards
    second pointer. Instead of using zeroes to move backward, I should
    instead use last_non_zero to move forward slower than current.
    """
    n = len(nums)
    if n <= 1:
        return nums
    zeroes = 0
    for current in range(1, n):
        if nums[current - 1] == 0:
            zeroes += 1
        if zeroes > 0:
            nums[current - zeroes] = nums[current]

    for i in range(n-1, n-1-zeroes, -1):
        nums[i] = 0

    return nums

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

    print(f" TEST CASE: Example 1 ".center(divider_width, "-"))
    tests += 1
    test_input = [0,1,0,3,12]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [1,3,12,0,0]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Example 2 ".center(divider_width, "-"))
    tests += 1
    test_input = [0]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [0]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: No Zeroes ".center(divider_width, "-"))
    tests += 1
    test_input = [1, 2, 3, 4]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [1, 2, 3, 4]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: All Zeroes ".center(divider_width, "-"))
    tests += 1
    test_input = [0, 0, 0, 0, 0]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [0, 0, 0, 0, 0]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Many Zeroes ".center(divider_width, "-"))
    tests += 1
    test_input = [0, 0, 0, 0, 0, 1]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [1, 0, 0, 0, 0, 0]
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Longer ".center(divider_width, "-"))
    tests += 1
    test_input = [0, 1, 2, 0, 4, 0, 5, 6, 7, 8, 9, 0, 10]
    print('Input:', test_input)
    result = solution(test_input)
    print('Output:', result)

    expected_result = [1, 2, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0]
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
