# Leetcode Problem #286
# Walls and Gates
# Andrew Tracey
# July 7, 2022

# CATEGORY
# BFS, Shortest Path

# PROBLEM DESCRIPTION
# You are given an m x n grid rooms initialized with these three possible values.
# > -1 A wall or an obstacle.
# > 0 A gate.
# > INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
#   represent INF as you may assume that the distance to a gate is less than
# 2147483647.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
# Input: rooms = [[2147483647,-1,0,2147483647]
#                 [2147483647,2147483647,2147483647,-1],
#                 [2147483647,-1,2147483647,-1],
#                 [0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:
# Input: rooms = [[-1]]
# Output: [[-1]]

# Constraints
# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 2^31 - 1.

# AT NOTES
# This is a shortest path problem, so we will use BFS. We will want to start
# our search from each gate, and at each level of the BFS, assign the shortest
# path as the value of each cell. To find the path to the nearest gate, we
# simply need to compare the values of the distance from each.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
from collections import deque

def solution(rooms):
    """Initial solution, using BFS"""
    m = len(rooms)
    n = len(rooms[0])
    q = deque()
    level = 0

    # discover the gates
    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                # include coordinates and distance from source gate in queue
                q.append((r, c, level))

    # initiate BFS
    while q:
        r, c, level = q.popleft()
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            i, j = r + d[0], c + d[1]
            if 0 <= i < m and 0 <= j < n:
                if level + 1 < rooms[i][j]:
                    rooms[i][j] = level + 1
                    q.append((i, j, level + 1))

    return rooms


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

    inf = 2147483647
    # Test Case Block
    test_case_description = 'Example 1'
    args = [[[inf,-1,0,inf],
             [inf,inf,inf,-1],
             [inf,-1,inf,-1],
             [0,-1,inf,inf]]]
    kwargs = {}
    expected_result = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[[-1]]]
    kwargs = {}
    expected_result = [[-1]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Larger Example'
    args = [[[0,inf,inf,-1,inf,inf],
             [-1,inf,inf,-1,-1,0],
             [-1,inf,inf,inf,inf,inf],
             [0,inf,inf,inf,inf,inf],
             [inf,inf,inf,-1,inf,inf],
             [inf,-1,inf,-1,inf,inf]]]
    kwargs = {}
    expected_result = [[0,1,2,-1,2,1],
                        [-1,2,3,-1,-1,0],
                        [-1,2,3,3,2,1],
                        [0,1,2,3,3,2],
                        [1,2,3,-1,4,3],
                        [2,-1,4,-1,5,4]]
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
