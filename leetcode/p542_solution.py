# 542 - Binary Matrix Distances
# https://leetcode.com/problems/01-matrix/

import math


class Solution:

    # list the methods to be run against the test cases
    implementations = ['get_nearest_zeroes']

    def get_nearest_zeroes(self, mat: list[list[int]]) -> list[list[int]]:
        """
        Dynamic Programming

        First, iterate over the matrix from top-left to bottom-right, updating
        the distance for each cell to the minimum of the distance for the cells
        above or to the left of it, plus 1. In this way, we are only relying
        on distances already calculated since the first cell (top-left) does not
        have adjancent cells above or to its left.

        Second, reverse iterate over the matrix from bottom-right to top-left,
        this time updating the distance for each cell to the minimum of a) the
        current distance, b) the minimum of the distances of the below and
        right cells + 1

        Time: O()
        Space: O()
        """
        
        # build the output matrix (problem asked for it in a separate list)
        ROWS = len(mat)
        COLS = len(mat[0])
        dist = [[0] * COLS for _ in range(ROWS)]

        # first loop, from top-left to bottom-right, moving row-wise
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
        
        # second loop, from bottom-right to top-left, moving row-wise
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

        return dist


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[[0, 0, 0],[0, 1, 0],[0, 0, 0]]],
            [[0, 0, 0],[0, 1, 0],[0, 0, 0]]],
        ['Example 2', [[[0, 0, 0],[0, 1, 0],[1, 1, 1]]],
            [[0, 0, 0],[0, 1, 0],[1, 2, 1]]],
        ['Large Input', [
            [
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1 ,1, 1],
            [1, 1, 1], [0, 0, 0]
            ]
        ],
        [
            [19, 19, 19], [18 ,18, 18], [17, 17, 17], [16, 16, 16],
            [15, 15, 15], [14 ,14, 14], [13, 13, 13], [12, 12, 12],
            [11, 11, 11], [10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7],
            [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1],
            [0, 0, 0]
        ]
        ]
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
