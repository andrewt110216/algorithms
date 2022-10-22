# 120 - Triangle (Minimum Falling Path Sum)
# https://leetcode.com/problems/triangle/

import math


class Solution:

    # list the methods to be run against the test cases
    implementations = ["get_min_sum_in_place", "get_min_sum_aux"]

    def get_min_sum_in_place(self, triangle: list[list[int]]) -> int:
        """
        Use dynamic programming to calculate the min sum for each cell in-place

        Time: O(n^2) one pass over triangle (n * (n-1) / 2)
        Space: O(1) no new data structures used
        """

        n = len(triangle)

        # iterate over the triangle, starting in the 2nd row
        for row in range(1, n):
            for col in range(row + 1):
                # find smallest min sum of parent cells
                parent_min = math.inf
                if col > 0:
                    parent_min = min(parent_min, triangle[row - 1][col - 1])
                if col < row:
                    parent_min = min(parent_min, triangle[row - 1][col])
                # update current cell value with its min falling path sum
                triangle[row][col] += parent_min

        # return the smallest minimum sum in the last row
        return min(triangle[-1])

    def get_min_sum_aux(self, triangle: list[list[int]]) -> int:
        """
        Use dynamic programming to calculate the min sum for each cell, using
        an array of length n to store the results

        Compared to the above 'in-place' solution, this addresses the case
        where we cannot modify the input array. Instead of creating a copy of
        the entire input array, we can accomplish our goal by using just a 1-D
        array of length n to store the minimum sums for the current row as we
        iterate over the triangle.

        Time: O(n^2) one pass over triangle (n * (n-1) / 2)
        Space: O(n) auxilary array to store results
        """

        n = len(triangle)

        # initialize our minimum sums array for the first row
        min_sums = [triangle[0][0]] + [math.inf for _ in range(n - 1)]

        # iterate over each row in triangle (starting with 2nd)
        for row in range(1, n):
            # move from right to left across the row to preserve prev min sums
            for col in range(row, -1, -1):
                # get min sum of right parent (or inf if out of bounds)
                parent_min = min_sums[col]
                # get min sum of left parent if in bounds
                if col > 0:
                    parent_min = min(parent_min, min_sums[col - 1])
                # calculate min sum of current cell and update min_sums
                min_sums[col] = triangle[row][col] + parent_min

        # return the smallest min sum
        return min(min_sums)


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]], 11],
        ["Example 2", [[[-10]]], -10],
        [
            "Slightly Larger",
            [[[1], [2, 3], [5, 4, 3], [6, 7, 5, 8], [10, 9, 11, 6, 7]]],
            18,
        ],
        ["Add Negatives", [[[-2], [3, 4], [-6, -5, -7], [4, 1, 8, 3]]], -4],
        [
            "Large Input",
            [
                [
                    [68],
                    [434, 940],
                    [588, 869, 500],
                    [806, 433, 806, 55],
                    [875, 458, 585, 123, 104],
                    [825, 414, 574, 476, 108, 172],
                    [553, 143, 311, 142, 753, 752, 729],
                    [140, 855, 707, 422, 37, 101, 117, 524],
                    [229, 839, 986, 207, 648, 175, 820, 240, 18],
                    [472, 859, 838, 117, 196, 498, 393, 364, 529, 997],
                    [98, 347, 457, 548, 807, 760, 609, 116, 607, 586, 874],
                    [
                        645,
                        840,
                        161,
                        183,
                        350,
                        746,
                        672,
                        322,
                        467,
                        642,
                        929,
                        790,
                    ],
                    [
                        642,
                        160,
                        350,
                        632,
                        134,
                        381,
                        44,
                        364,
                        266,
                        167,
                        151,
                        987,
                        855,
                    ],
                    [
                        10,
                        104,
                        168,
                        614,
                        769,
                        899,
                        15,
                        269,
                        379,
                        862,
                        924,
                        839,
                        106,
                        579,
                    ],
                    [
                        240,
                        966,
                        88,
                        866,
                        292,
                        224,
                        136,
                        883,
                        344,
                        29,
                        473,
                        418,
                        329,
                        124,
                        636,
                    ],
                    [
                        859,
                        89,
                        582,
                        291,
                        14,
                        586,
                        391,
                        157,
                        613,
                        316,
                        840,
                        914,
                        61,
                        942,
                        899,
                        100,
                    ],
                    [
                        946,
                        741,
                        10,
                        996,
                        708,
                        576,
                        407,
                        776,
                        826,
                        467,
                        476,
                        699,
                        21,
                        749,
                        952,
                        155,
                        105,
                    ],
                    [
                        330,
                        404,
                        576,
                        447,
                        151,
                        577,
                        765,
                        640,
                        636,
                        797,
                        647,
                        795,
                        209,
                        570,
                        362,
                        348,
                        108,
                        938,
                    ],
                    [
                        283,
                        826,
                        303,
                        42,
                        307,
                        482,
                        418,
                        95,
                        388,
                        844,
                        811,
                        620,
                        177,
                        919,
                        503,
                        435,
                        636,
                        406,
                        786,
                    ],
                ]
            ],
            5469,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
