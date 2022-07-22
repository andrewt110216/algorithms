# 200 - Number of Islands
# https://leetcode.com/problems/number-of-islands/

from collections import deque


class Solution:

    # list the methods to be run against the test cases
    implementations = ['count_islands_bfs', 'count_islands_dfs']

    def count_islands_bfs(self, grid: list[list[int]]) -> int:
        """
        Use breadth first search

        Iterate over each cell of the grid. When land is found, perform a bfs
        to 4-directionally adjacent land cells. As land cells are discovered,
        label them as `conquered` by changing their value to 0. This will
        prevent us from rediscovering the same island again

        Time: O(m * n) (if grid is all land)
        Space: O(min(m, n)) (maximum size of the queue)
        """

        # initialize dimensions and number of islands
        m = len(grid)
        n = len(grid[0])
        islands = 0

        # helper function to perform breadth-first-search
        def bfs(row, col):

            # initiate new queque for bfs from row, col
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()

                # check each 4-directionally adjacent cell for land
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i, j = r + d[0], c + d[1]

                    # validate that (i, j) is `in-bounds` then check for land
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":

                        # change land to water and add (i, j) to queque
                        grid[i][j] = "0"
                        q.append((i, j))

        # iterate over each cell of the grid
        for r in range(m):
            for c in range(n):

                # if a cell is land, it is a new island
                # perform bfs to `conquer` the entire island
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)

        return islands

    def count_islands_dfs(self, grid: list[list[int]]) -> int:
        """
        Use depth first search

        Iterate over each cell of the grid. When land is found, perform a dfs
        to 4-directionally adjacent land cells. As land cells are discovered,
        label them as `conquered` by changing their value to 0. This will
        prevent us from rediscovering the same island again

        Time: O(m * n) (iterate over all cells of the grid)
        Space: O(m * n) (length of first DFS if grid is all land)
        """

        # initialize dimensions and number of islands
        m = len(grid)
        n = len(grid[0])
        islands = 0

        # helper function to perform depth-first-search
        def dfs(r, c):

            # validate that (r, c) is `in-bounds` then check for land
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            # change land to water, and dfs on 4-directionally adjacent cells
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # iterate over each cell of the grid
        for r in range(m):
            for c in range(n):

                # if a cell is land, it is a new island
                # perform dfs to `conquer` the entire island
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            'Example 1',
            [
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]
                ]
            ],
            1
        ],
        [
            'Example 2',
            [
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"]
                ]
            ],
            3
        ],
        ['Small Island', [[["1"]]], 1],
        ['Small Water', [[["0"]]], 0],
        [
            'All Land',
            [
                [
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"]
                ]
            ],
            1
        ],
        [
            'All Water',
            [
                [
                    ["0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]
                ]
            ],
            0
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
