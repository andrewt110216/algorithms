# Leetcode Problem #733
# Flood Fill
# Andrew Tracey
# May 15, 2022

# CATEGORY
# Depth-First-Search (DFS)

# PROBLEM DESCRIPTION
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel 
# value of the image.
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the
# image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
# to the starting pixel of the same color as the starting pixel, plus any pixels connected
# 4-directionally to those pixels (also with the same color), and so on. Replace the color of
# all of the aforementioned pixels with newColor.
# Return the modified image after performing the flood fill.

# Example 1:
#  ---------    ---------
# | 1  1  1 |  | 2  2  2 |
# | 1  1  0 |  | 2  2  0 |
# | 1  0  1 |  | 2  0  1 |
#  ---------    ---------
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1), all pixels connected
# by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with
# the new color. Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]

# Constraints
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 216
# 0 <= sr < m
# 0 <= sc < n

# AT NOTES
# First, will attempt a recursive solution. The steps will be to first update the color of the
# starting pixel. Then, determine the possible, in-bounds, 4-direction connections (helper function).
# Importantly, remove any previously visited pixels from these connections, since we do not want to
# move left, then move back to the right.
# Now, for each valid and new connection, evaluate if the color matches the starting color. If so,
# update it, and recurse on that pixel to evaluate it's connections.
# Return the final image.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    """Recursive solution. Attempt #1."""
    
    # helper function to check for in-bounds 4-directional connections
    def get_connections(row, column):
        connections = set()
        # check left
        if column - 1 >= 0:
            connections.add((row, column - 1))
        # check right
        if column + 1 < len(image[0]):
            connections.add((row, column + 1))
        # check above
        if row - 1 >= 0:
            connections.add((row - 1, column))
        # check below
        if row + 1 < len(image):
            connections.add((row + 1, column))
        return connections
    
    # helper recursive function to recurse over connections with matching color
    def recurse(row, column):
        
        connections = get_connections(row, column)
        # ignore connections that we already visited
        connections = connections - visited
        
        # evaluate each connection
        for r, c in connections:
            visited.add((row, column))
            if image[r][c] == scolor:
                image[r][c] = newColor
                recurse(r, c)
        
        return image
    
    # Save initial color of starting pixel, then change it's color
    scolor = image[sr][sc]
    image[sr][sc] = newColor
    visited = set((sr, sc))
    
    # Initiate recursion, from the starting pixel
    return recurse(sr, sc)


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
    args = [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2]
    kwargs = {}
    expected_result = [[2,2,2],[2,2,0],[2,0,1]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[[0,0,0],[0,0,0]], 0, 0, 2]
    kwargs = {}
    expected_result = [[2,2,2],[2,2,2]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Small Inputs'
    args = [[[1],[1]], 0, 0, 2]
    kwargs = {}
    expected_result = [[2],[2]]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Larger Inputs'
    args = [[[0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1], 
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0]], 0, 3, 2]
    kwargs = {}
    expected_result =  [[0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0],
                        [2, 2, 2, 2, 2, 2, 2], 
                        [0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 2, 0, 0, 0]]
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
