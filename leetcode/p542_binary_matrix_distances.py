# Leetcode Problem #542
# 01 Matrix
# Andrew Tracey
# May 19, 2022

# CATEGORY
# Array, Dynamic Programming

# PROBLEM DESCRIPTION
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Constraints
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
import collections
import math

def solution(mat: list[list[int]]) -> list[list[int]]:
    """DYNAMIC PROGRAMMING - ACCEPTED"""
    # First, iterate over the matrix from top-left to bottom-right, updating
    # the distance for each cell to the minimum of the distance for the cells
    # above or to the left of it, plus 1. In this way, we are only relying
    # on distances already calculated since the first cell (top-left) does not
    # have adjancent cells above or to its left.
    # Second, reverse iterate over the matrix from bottom-right to top-left,
    # this time updating the distance for each cell to the minimum of a) the 
    # current distance, b) the minimum of the distances of the below and right
    # cells + 1
    
    # build the output matrix (problem asked for it in a separate list)
    ROWS = len(mat)
    COLS = len(mat[0])
    dist = [[0] * COLS for _ in range(ROWS)]

    # first loop, from top-left to bottom-right, moving row-wise
    if debug: print(' > Beginning first loop, forward...')
    for i in range(ROWS):
        for j in range(COLS):
            if mat[i][j]:  # skip if 0, as default dist is 0
                top = left = math.inf
                # get top
                if i > 0:
                    top = dist[i-1][j]
                # get left
                if j > 0:
                    left = dist[i][j-1]
                # take minimum of top, left, and add 1
                dist[i][j] = min(top, left) + 1
            if debug:
                print(f'  > Updated row {i}, column{j}. Distances:')
                for row in dist:
                    print('    ', row)
    
    # second loop, from bottom-right to top-left, moving row-wise
    if debug: print(' > Beginning second loop, reverse...')
    for i in range(ROWS-1, -1, -1):
        for j in range(COLS-1, -1, -1):
            if mat[i][j]:  # again, skip 0's. No work to do.
                below = right = math.inf
                # get below
                if i + 1 < ROWS:
                    below = dist[i+1][j]
                # get right
                if j + 1 < COLS:
                    right = dist[i][j+1]
                # take minimum of current val, below + 1, right + 1
                dist[i][j] = min(dist[i][j], below + 1, right + 1)
            if debug:
                print(f'  > Updated row {i}, column{j}. Distances are now:')
                for row in dist:
                    print('    ', row)
    return dist

def solution2(mat: list[list[int]]) -> list[list[int]]:
    """BRUTE FORCE - DOUBLE FOR LOOP - TIME LIMITED EXCEEDED (TLE)"""
    # This was my second implementation, which is really the most intuitive
    # approach, of using two for loops to calculate the distances to all 0's 
    # for each cell, and taking the minimum distance.
    # It works, and really isn't too slow except for huge inputs.
    
    # build the output matrix
    ROWS = len(mat)
    COLS = len(mat[0])
    out = [[0] * COLS for _ in range(ROWS)]
    
    # outer for loop to iterate over each cell
    for r in range(ROWS):
        for c in range(COLS):
            # skip cell if value is 0 (distance already set to 0)
            if mat[r][c]:
                # use for loop to calculate distance to each 0, tracking min
                min_dist = math.inf
                for i in range(ROWS):
                    for j in range(COLS):
                        if mat[i][j] == 0:
                            dist = abs(r - i) + abs(c - j)
                            min_dist = min(min_dist, dist)
                out[r][c] = min_dist

    return out

def solution1(mat: list[list[int]]) -> list[list[int]]:
    """BRUTE FORCE WITH BFS - MEMORY LIMITED EXCEEDED (MLE)"""
    # This was my first implementation. While it does quickly solve the two 
    # example inputs, it takes FOREVER on a larger input where there are a lot
    # of 1's and the distances are generally high. Running this solution on 
    # the 'Large Input' test case, I don't even get through the first cell
    # before reaching max recursion depth. Yikes. This is actually a terrible
    # solution, and significantly worse than the more brute force implementation
    # of doing a nested for loop to calculate the distance to every 0 from each
    # cell, and take the minimum. See solution2.

    # Iterate over matrix, perform BFS from each point, and populate
    # distance to 0 into output matrix
    
    # build the output matrix
    ROWS = len(mat)
    COLS = len(mat[0])
    out = [[None] * COLS for _ in range(ROWS)]
    
    # helper function to check for in-bounds connections, add to queque
    def add_connections(r, c):
        if r > 0:
            q.append((r-1, c))
        if r + 1 < ROWS:
            q.append((r+1, c))
        if c > 0:
            q.append((r, c-1))
        if c + 1 < COLS:
            q.append((r, c+1))
    
    if debug: print(' > Starting Iteration of Matrix...')
    for r in range(ROWS):
        for c in range(COLS):
            if debug: print(f'  > Current Cell is mat[{r}][{c}] ({mat[r][c]})')
            # create stack for BFS
            q = collections.deque([(r, c)])
            while q:
                i, j = q.popleft()
                if mat[i][j] == 0:
                    # calculate distance from r, c
                    dist = abs(r - i) + abs(c - j)
                    out[r][c] = dist
                    if debug: print(f'    > Dist for cell ({i}, {j}) = {dist}')
                    break
                else:
                    add_connections(i, j)
            if debug:
                print('  > Out Matrix is currently:')
                for row in out:
                    print('   ', row)
    
    return out


# =============================== DRIVER CODE ================================

if __name__ == '__main__':
    from datetime import datetime

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements, if any
    debug = True

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
            print('Time:', datetime.now()-start)

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
    args = [[[0,0,0],[0,1,0],[0,0,0]]]
    kwargs = {}
    expected_result = [[0,0,0],[0,1,0],[0,0,0]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[[0,0,0],[0,1,0],[1,1,1]]]
    kwargs = {}
    expected_result = [[0,0,0],[0,1,0],[1,2,1]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Large Input'
    args = [[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],
             [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],
             [1,1,1],[1,1,1],[1,1,1],[0,0,0]]]
    kwargs = {}
    expected_result = [[19,19,19],[18,18,18],[17,17,17],[16,16,16],
                       [15,15,15],[14,14,14],[13,13,13],[12,12,12],[11,11,11],
                       [10,10,10],[9,9,9],[8,8,8],[7,7,7],[6,6,6],[5,5,5],
                       [4,4,4],[3,3,3],[2,2,2],[1,1,1],[0,0,0]]
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
