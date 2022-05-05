# Leetcode Problem #20
# Valid Parentheses
# Andrew Tracey
# May 4, 2022

# CATEGORY
# Stacks

# PROBLEM DESCRIPTION
# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
# An input string is valid if:
#  - Open brackets must be closed by the same type of brackets.
#  - Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

# AT NOTES
# Use a stack. For each open bracket, push it to the stack.
# When we encounter a closed bracket, we need to pop from the stack and make
# sure that the popped bracket opens the closed bracket. If not, return False.
# If the stack is empty while still traversing s, return False.
# If we reach the end of s and the stack is empty, return False.
# Use collections.deque for the stack

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
import collections

def solution(s):
    """Use a stack to confirm brackets are closed correctly"""

    stack = collections.deque()

    # Iterate over each character in s
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:  # By constraints, char is a closing bracket in [")", "]", "}"]
            
            # If the stack is empty, this closed bracket was not last opened
            if len(stack) <= 0:
                return False

            # Pop from stack and make sure it is the appropriate open bracket
            removed = stack.pop()
            if char == ")" and removed != "(":
                return False
            if char == "]" and removed != "[":
                return False
            if char == "}" and removed != "{":
                return False

    # If the stack is not empty, then an open bracket was not properly closed
    if len(stack) == 0:
        return True
    return False


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

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

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = ["()"]
    kwargs = {}
    expected_result = True
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = ["()[]{}"]
    kwargs = {}
    expected_result = True
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = ["(]"]
    kwargs = {}
    expected_result = False
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Nested Example - Correct'
    args = ["([{()}])"]
    kwargs = {}
    expected_result = True
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Nested Example - Incorrect'
    args = ["([{()}[])"]
    kwargs = {}
    expected_result = False
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
