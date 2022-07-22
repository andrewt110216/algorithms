# 286 - Walls and Gates
# https://leetcode.com/problems/walls-and-gates/

from collections import deque


class Solution:

    # list the methods to be run against the test cases
    implementations = ['walls_and_gates']

    def walls_and_gates(self, rooms: list[list[int]]) -> list[list[int]]:
        """
        This is a shortest path problem, so we will use bread-first-search

        We need to start a search from each gate, and at each level of the BFS,
        assign the shortest path as the value of each cell

        Time: O(m * n) (each room is visited at most once)
        Space: O(m * n) (max size of the queue)
        """

        # create variables for height and width of grid
        m = len(rooms)
        n = len(rooms[0])

        # create queue for BFS and distance to measure steps from gate
        q = deque()
        distance = 0

        # first, we must iterate over the grid in order to discover all gates
        # and add them to the front of the queue
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:

                    # q includes grid coordinates and distance from source gate
                    q.append((r, c, 0))

        # initiate BFS
        while q:
            r, c, distance = q.popleft()

            # check all 4-directionally adjacent cells
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = r + d[0], c + d[1]

                # validate that i and j are `in-bounds`
                if 0 <= i < m and 0 <= j < n:

                    # compare current distance to current value of room
                    # 1. room is a wall (-1) => distance can't be less than -1
                    # 2. room is a gate (0) => distance + 1 can't be < 0
                    # 3. room is empty (inf) => distance can't be more than inf
                    # 4. room was already discovered and assigned a distance =>
                    #    - only update it if current distance is shorter
                    if distance + 1 < rooms[i][j]:
                        rooms[i][j] = distance + 1

                        # add to q to continue bfs
                        q.append((i, j, distance + 1))

        return rooms


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    inf = 2147483647
    test_cases = [
        [
            'Example 1',
            [
                [
                    [inf, -1, 0, inf],
                    [inf, inf, inf, -1],
                    [inf, -1, inf, -1],
                    [0, -1, inf, inf]
                ]
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ]
        ],
        [
            'Example 2',
            [
                [
                    [-1],
                ]
            ],
            [
                [-1],
            ]
        ],
        [
            'Larger Grid',
            [
                [
                    [0, inf, inf, -1, inf, inf],
                    [-1, inf, inf, -1, -1, 0],
                    [-1, inf, inf, inf, inf, inf],
                    [0, inf, inf, inf, inf, inf],
                    [inf, inf, inf, -1, inf, inf],
                    [inf, -1, inf, -1, inf, inf],
                ]
            ],
            [
                [0, 1, 2, -1, 2, 1],
                [-1, 2, 3, -1, -1, 0],
                [-1, 2, 3, 3, 2, 1],
                [0, 1, 2, 3, 3, 2],
                [1, 2, 3, -1, 4, 3],
                [2, -1, 4, -1, 5, 4],
            ]
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
