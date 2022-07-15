# Leetcode Problem #77
# Combinations
# Andrew Tracey
# July 15, 2022

# CATEGORY
# Backtracking

# PROBLEM DESCRIPTION
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]

# Constraints
# 1 <= n <= 20
# 1 <= k <= n

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
# if using multiple solutions, name the function you want to use 'solution',
# and change the name of other functions (e.g. 'solution1', 'solution2', etc.)

def solution(n: int, k: int) -> list[list[int]]:
    """Backtracking"""
    # time complexity: O(n choose k)
    #  - by adding the return statement in the base case, we ensure that each
    #    combination is generated exactly once, making the number of recursive
    #    calls n choose k. The append and pop operations are both O(1).
    # space complexity: O(n choose k)
    #  - the size of the call stack, by the same reasoning as time complexity

    def backtrack(first, cur):
        # if the combination is done
        if len(cur) == k:  
            output.append(cur[:])
            return None  # add return to prevent list from growing past len k
        for i in range(first, n + 1):
            # add i into the current combination
            cur.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, cur)
            # backtrack
            cur.pop()

    output = []
    backtrack(1, [])
    return output

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
            result = sorted(func(*args, **kwargs))
            print('Output:', result)
            print('Time:', datetime.now() - start)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected}\n")
                failed_tests += 1

        return wrapper

    # For testing, decorate the solution function
    solution = test_decorator(solution)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = [4, 2]
    kwargs = {}
    expected_result = sorted([[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]])
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [1, 1]
    kwargs = {}
    expected_result = [[1]]
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
