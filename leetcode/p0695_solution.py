# 695 - Max Area of Island
# https://leetcode.com/problems/max-area-of-island/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["solution"]  # **UPDATE LIST AND DELETE THIS COMMENT**

    def solution(self, grid: list[list[int]]) -> int:
        """
        We will traverse the grid row-wise, and at each cell, if it is a 1, we
        will perform a depth-first-search (iterative, using a stack) to check
        each 4-directionally adjacent cell and keep track of the area of the
        island. We will update the maximum area as we go. Keeping track of the
        cells visited in a set will prevent us from visiting the same cell more
        than once, whether it is a 0 (no need to revisit) or a 1 (only needs to
        be visited once for each along to which it belongs, which is by
        definition 1).

        Time: O()
        Space: O()
        """

        max_area = 0
        visited = set()
        R = len(grid)
        C = len(grid[0])

        for row in range(R):
            for col in range(C):
                if (row, col) not in visited and grid[row][col] == 1:
                    stack = [(row, col)]
                    visited.add((row, col))
                    cur_area = 0
                    while stack:
                        r, c = stack.pop()
                        cur_area += 1
                        neighbors = [
                            (r - 1, c),
                            (r + 1, c),
                            (r, c - 1),
                            (r, c + 1),
                        ]
                        for r_adj, c_adj in neighbors:
                            if (
                                (0 <= r_adj < R and 0 <= c_adj < C)
                                and grid[r_adj][c_adj] == 1
                                and (r_adj, c_adj) not in visited
                            ):
                                stack.append((r_adj, c_adj))
                                visited.add((r_adj, c_adj))
                    max_area = max(max_area, cur_area)

        return max_area


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ]
            ],
            6,
        ],
        ["Example 2", [[[0, 0, 0, 0, 0, 0, 0, 0]]], 0],
        ["Example 2 - With Island", [[[0, 0, 0, 1, 1, 0, 0, 0]]], 2],
        [
            "Larger Example",
            [
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ]
            ],
            22,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
