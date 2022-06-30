# Leetcode Problem #344
# Reverse String
# Andrew Tracey
# June 30, 2022

# CATEGORY
# Two Pointers

# PROBLEM DESCRIPTION
# Write a function that reverses a string. The input string is given as an array
# of characters s. You must do this by modifying the input array in-place with
# O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.

# AT NOTES
# Use two pointers, starting at each end of the array and moving inwards.
# Consider element 0 and n - 1 as 'opposite' around the center. Swap them, then
# move on to elements 1 and n - 2.
# This can be done either with two explicitly defined pointers and a while loop
# stopping when left == right, or with a for loop on the first half of the 
# elements, since the second pointer can always be calculated from the left
# element, i, as n - 1 - i.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(s):
    """Two pointers. While loop."""
    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

def solution1(s):
    """Two pointers. For loop, calculating second pointer each time"""
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
    return s

# =============================== DRIVER CODE ================================

if __name__ == '__main__':
    from datetime import datetime

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements, if any
    debug = False

    tests = 0
    failed_tests = 0
    divider_width = 78

# Decorator Function for Testing Output --------------------------------------

    def test_decorator(func):
        """Decorator function to wrap around the solution"""
        def wrapper(expected, description, *args, **kwargs):
            global tests, failed_tests, divider_width
            tests += 1
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            print('Input:', *args, **kwargs)
            start = datetime.now()
            result = func(*args, **kwargs)
            print('Output:', result)
            print('Time:', datetime.now() - start)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_result}\n")
                failed_tests += 1

        return wrapper

    # For testing, decorate the solution function
    solution = test_decorator(solution)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = [["h","e","l","l","o"]]
    kwargs = {}
    expected_result = ["o","l","l","e","h"]
    solution(expected_result, test_case_description, *args, **kwargs)

#    # Test Case Block
    test_case_description = 'Example 2'
    args = [["H","a","n","n","a","h"]]
    kwargs = {}
    expected_result = ["h","a","n","n","a","H"]
    solution(expected_result, test_case_description, *args, **kwargs)

#    # Test Case Block
    test_case_description = 'Single Element'
    args = [["a"]]
    kwargs = {}
    expected_result = ["a"]
    solution(expected_result, test_case_description, *args, **kwargs)

#    # Test Case Block
    test_case_description = 'Two Element'
    args = [["a", "b"]]
    kwargs = {}
    expected_result = ["b", "a"]
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
