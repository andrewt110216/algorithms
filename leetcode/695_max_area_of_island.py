# Leetcode Problem #695
# Max Area of Island

# CATEGORY
# Depth-First-Search

# PROBLEM DESCRIPTION
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the
# grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input:
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0]
#         [0,1,1,0,1,0,0,0,0,0,0,0,0]
#         [0,1,0,0,1,1,0,0,1,0,1,0,0] -|
#         [0,1,0,0,1,1,0,0,1,1,1,0,0]  |<- largest island (area 6)
#         [0,0,0,0,0,0,0,0,0,0,1,0,0] -|
#         [0,0,0,0,0,0,0,1,1,1,0,0,0]
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# # Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

# AT NOTES
# We will traverse the grid row-wise, and at each cell, if it is a 1, we will perform
# a depth-first-search (iterative, using a stack) to check each 4-directionally adjacent cell
# and keep track of the area of the island. We will update the maximum area as we go.
# Keeping track of the cells visited in a set will prevent us from visiting the same cell more
# than once, whether it is a 0 (no need to revisit) or a 1 (only needs to be visited once for
# each along to which it belongs, which is by definition 1).

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(grid: list[list[int]]) -> int:
    """Solution #1: Iterative Depth-First-Search"""
    R = len(grid)
    C = len(grid[0])
    visited = set()
    max_area = 0
    row = 0
    while row < R:
        column = 0
        while column < C:
            # check if we're at a 1 that we haven't yet been to
            if (row, column) not in visited and grid[row][column] == 1:
                # now, let's find the island size
                cur_area = 0
                stack = []
                stack.append((row, column))
                while stack:
                    r, c = stack.pop()
                    if grid[r][c] == 1 and (r, c) not in visited:
                        visited.add((r, c))
                        cur_area += 1
                        max_area = max(max_area, cur_area)
                        # check 4-directional connections
                        if r >= 1 and (r - 1, c) not in visited: # above
                            stack.append((r - 1, c))
                        if r + 1 < R and (r + 1, c) not in visited: # below
                            stack.append((r + 1, c))
                        if c >= 1 and (r, c - 1) not in visited: # left
                            stack.append((r, c - 1))
                        if c + 1 < C and (r, c + 1) not in visited: # right
                            stack.append((r, c + 1))
            else:
                visited.add((row, column))
                column += 1
        row += 1
    
    return max_area


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
    args = [[[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]]
    kwargs = {}
    expected_result = 6
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[[0,0,0,0,0,0,0,0]]]
    kwargs = {}
    expected_result = 0
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2 - With Island'
    args = [[[0,0,0,1,1,0,0,0]]]
    kwargs = {}
    expected_result = 2
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Another Example'
    args = [[[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,1,0,0,0,1,1,0,0],
             [0,0,0,0,0,1,1,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]]
    kwargs = {}
    expected_result = 22
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
