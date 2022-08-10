# 931 - Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

from functools import lru_cache
import math


class Solution:

    # list the methods to be run against the test cases
    implementations = ["get_min_path_dp", "get_min_path_recursive"]

    def get_min_path_dp(self, matrix: list[list[int]]) -> int:
        """
        Use dynamic programming, updating the matrix in-place

        Loop once over the entire matrix, and at each cell calculate the min
        falling path sum for that cell and update it in place. The min sum for
        a given cell can then simply be calculated as the current value plus
        the smallest min sum for its 'parent' cells, where 'parent' cells
        refers to the cells in the previous row that could possibly fall to the
        current cell.

        Time: O(n^2) only one loop over the matrix
        Space: O(1) only constant extra space is used
        """

        n = len(matrix)

        # loop over the matrix, starting in the 2nd row
        for i in range(1, n):
            for j in range(n):
                # find smallest min sum for parent cells
                parent_min = matrix[i - 1][j]
                if j > 0:
                    parent_min = min(parent_min, matrix[i - 1][j - 1])
                if j + 1 < n:
                    parent_min = min(parent_min, matrix[i - 1][j + 1])
                # update current cell with its min falling path sum
                matrix[i][j] += parent_min

        return min(matrix[-1])

    def get_min_path_recursive(self, matrix: list[list[int]]) -> int:
        """
        Recursive implementation, using memoization

        The problem sets up well for recursion. We can find the min falling
        path sum ending at each cell in the final row recursively, and then
        return the minimum of those sums.

        At each cell, the min falling path is equal to the smallest min falling
        path through its 'parent' cells plus its own value, where 'parent'
        cells refers to the cells in the previous row that could possibly fall
        to the current cell.

        The base case of our recursive function will be when we reach the first
        row, in which case there are no parent cells.

        Finally, to optimize the recursive function we use memoization by way
        of the lru_cache method of the functools built-in library. This will
        save the results of our min sum calculations for each cell, so that we
        don't repeat the same work.

        Time: O(n^2) calculate the min falling path once for each cell
         - thanks to memoization, our recursive calls will get cutoff once we
           see a problem we have already tackled. therefore, we will only
           initiate a call from each cell once
        Space: O(n^2) max size of call stack
         - on the first call (recurse(n-1, 0)), there will be n levels of
           recursive calls, where (thanks to memoization) each level has just
           1 new piece of work to do. Therefore, the size of the call stack
           will be n + (n - 1) + (n - 2) + ... + 1 = n * (n-1) / 2 = O(n^2)
         - on successive calls from row n - 1 (again thanks to memoization),
           we will only have one new min sum to calculate per level
        """

        n = len(matrix)

        @lru_cache
        def recurse(r, c):
            # base case: in the first row, min sum is the cell value
            if r == 0:
                return matrix[r][c]

            # find min sum through parent cells
            parent_min = recurse(r - 1, c)
            if c > 0:
                parent_min = min(parent_min, recurse(r - 1, c - 1))
            if c + 1 < n:
                parent_min = min(parent_min, recurse(r - 1, c + 1))

            return parent_min + matrix[r][c]

        # find min sum ending at each cell in the final row
        # pick the minimum of those sums as the overall min sum
        overall_min = math.inf
        for c in range(n):
            local_min = recurse(n - 1, c)
            overall_min = min(overall_min, local_min)

        return overall_min


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[[2, 1, 3], [6, 5, 4], [7, 8, 9]]], 13],
        ["Example 2", [[[-19, 57], [-40, -5]]], -59],
        ["Example 1 V2", [[[2, 1, 3], [6, 5, 4], [7, 8, 7]]], 12],
        [
            "Large Input",
            [
                [
                    [80, 76, 17, 83, 71, 63, 19, 68, 23, 34, 97, 98],
                    [52, 41, 88, 49, 54, 95, 23, 26, 11, 39, 93, 45],
                    [41, 46, 21, 22, 30, 73, 84, 68, 47, 65, 88, 74],
                    [42, 71, 70, 44, 99, 41, 50, 69, 61, 27, 91, 49],
                    [59, 47, 56, 49, 67, 75, 38, 25, 11, 66, 64, 61],
                    [75, 68, 64, 33, 59, 68, 86, 47, 33, 54, 57, 31],
                    [68, 90, 40, 53, 69, 38, 83, 42, 92, 77, 42, 28],
                    [15, 35, 81, 71, 54, 68, 92, 34, 19, 62, 90, 72],
                    [97, 23, 73, 29, 85, 68, 58, 17, 94, 57, 49, 23],
                    [68, 49, 45, 86, 23, 21, 58, 31, 92, 34, 34, 71],
                    [50, 21, 62, 36, 72, 73, 71, 51, 54, 36, 57, 90],
                    [17, 86, 84, 39, 59, 68, 11, 34, 19, 62, 21, 11],
                ]
            ],
            323,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
