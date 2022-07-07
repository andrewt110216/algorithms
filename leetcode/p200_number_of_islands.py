# Leetcode Problem #200
# Number of Islands
# Andrew Tracey
# July 7, 2022

# CATEGORY
# DFS

# PROBLEM DESCRIPTION
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are
# all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# AT NOTES
# DFS is an intuitive approach to 'conquer' an entire island. In order to 
# discover all islands and count them, we will loop through the entire grid
# searching for land. When we find land, we will 'conquer' the island, changing
# 1's to 0's, so that we do not re-conquer the island when we return to the
# outer loops. Since each entire island is 'hidden' after we conquer it, each
# time we find new land in the loops, it is a new island, so we increment our
# count.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(grid):
    m = len(grid)
    n = len(grid[0])
    islands = 0
    
    def dfs(r, c):
        """DFS from grid[r][c] to valid cells with value 1"""
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    
    # search grid for land, and conquer each island as it is discovered
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                islands += 1
                dfs(r,c)
    return islands


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
    args = [[["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]]
    kwargs = {}
    expected_result = 1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]]
    kwargs = {}
    expected_result = 3
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Small Island'
    args = [[["1"]]]
    kwargs = {}
    expected_result = 1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Small Water'
    args = [[["0"]]]
    kwargs = {}
    expected_result = 0
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'All Land'
    args = [[["1","1","1","1"],
             ["1","1","1","1"],
             ["1","1","1","1"],
             ["1","1","1","1"]]]
    kwargs = {}
    expected_result = 1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'All Water'
    args = [[["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"]]]
    kwargs = {}
    expected_result = 0
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
