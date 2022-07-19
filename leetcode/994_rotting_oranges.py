# Leetcode Problem #994
# Rotting Oranges

# CATEGORY
# Array, BFS

# PROBLEM DESCRIPTION
# You are given an m x n grid where each cell can have one of three values:
# - 0 representing an empty cell, 
# - 1 representing a fresh orange, or
# - 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten. Return the minimum number of minutes that must elapse
# until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.

# Constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


# AT NOTES
# Notice that each minute correspondes to going one layer further in a BFS, 
# starting from a rotten orange. In fact, a BFS should begin at minute 0 from
# each initially rotten orange. The task, then, is to to perform this BFS, and
# at the end of each level, check if there are any good oranges left.
# If not, then return the current minute.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
import collections

def solution(grid):
    """Second solution, removing use of deque and visited cells"""
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    #  - in worst case, the list of rotten oranges could be every cell

    m = len(grid)
    n = len(grid[0])
    
    # get initial rotten oranges and count fresh ones
    current_level = []
    fresh = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                current_level.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    # update rotten oranges one BFS level at a time
    minute = 0
    while current_level and fresh:
        minute += 1
        next_level = []
        for r, c in current_level:
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i, j = r + d[0], c + d[1]
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        next_level.append((i, j))
        current_level = next_level
    
    if fresh:
        return -1
    else:
        return minute


def solution1(grid):
    """Initial solution"""
    # time complexity: 2 * O(m * n) (discovery, then BFS) = O(m * n)
    # space complexity: 2 * O(m * n) (queue, visited cells) = O(m * n)

    R = len(grid)
    C = len(grid[0])

    def discover_oranges(grid):
        """Return the locations of rotten oranges and a count of fresh ones"""
        rottens = []
        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottens.append((r, c))
        return rottens, fresh
    
    def get_adjacent_cells(row, col):
        """Return a list of the valid 4-directionally adjacent cells"""
        cells = []
        # left
        if col > 0:
            cells.append((row, col - 1))
        # right
        if col + 1 < C:
            cells.append((row, col + 1))
        # above
        if row > 0:
            cells.append((row - 1, col))
        # below
        if row + 1 < R:
            cells.append((row + 1, col))
        return cells

    minute = 0
    rottens, fresh = discover_oranges(grid)
    q = collections.deque([rottens])
    visited_cells = set()

    # process rotting oranges, one minute at a time
    while len(q) > 0 and fresh > 0:
        cur_rottens = q.popleft()
        if len(cur_rottens) == 0:
            break
        minute += 1
        new_rottens = []
        for rotten in cur_rottens:
            visited_cells.add(rotten)
            # update adjacent oranges to rotten
            adjacent_cells = get_adjacent_cells(*rotten)
            for r, c in adjacent_cells:
                if (r, c) not in visited_cells:
                    visited_cells.add((r, c))
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        new_rottens.append((r, c))
                        fresh -= 1
        q.append(new_rottens)

    # all possible oranges have rotted. check for any good oranges.
    if fresh > 0:
        return -1
    else:
        return minute


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
    args = [[[2,1,1],[1,1,0],[0,1,1]]]
    kwargs = {}
    expected_result = 4
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[[2,1,1],[0,1,1],[1,0,1]]]
    kwargs = {}
    expected_result = -1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = [[[0,2]]]
    kwargs = {}
    expected_result = 0
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Multiple Rotten To Start'
    args = [[[2,1,1,1],[1,1,0,0],[0,1,0,2],[1,1,0,1],[0,0,1,1]]]
    kwargs = {}
    expected_result = 5
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
