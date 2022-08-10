# 994 - Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["oranges_rotting"]

    def oranges_rotting(self, grid: list[list[int]]) -> int:
        """
        Use breadth-first-search

        Notice that each minute corresponds to one additional level in a BFS,
        starting from each initially rotten orange. At the end of each level,
        we will check if there are any fresh oranges left.

        Time: O(m * n) (we might visit every cell in the grid once)
        Space: O(m * n) (starting size of the queue if all oranges are rotten)
        """

        m = len(grid)
        n = len(grid[0])

        # discover initial rotten oranges and count fresh ones
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
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        next_level.append((i, j))
            current_level = next_level

        return -1 if fresh else minute


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], 4],
        ["Example 1", [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], -1],
        ["Example 3", [[[0, 2]]], 0],
        [
            "Multiple Rotten to Start",
            [
                [
                    [2, 1, 1, 1],
                    [1, 1, 0, 0],
                    [0, 1, 0, 2],
                    [1, 1, 0, 1],
                    [0, 0, 1, 1],
                ]
            ],
            5,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
