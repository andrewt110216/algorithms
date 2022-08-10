# 733 - Flood Fill
# https://leetcode.com/problems/flood-fill/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["flood_fill_iterative", "flood_fill_recursive"]

    def flood_fill_iterative(
        self, image: list[list[int]], sr: int, sc: int, new_color: int
    ) -> list[list[int]]:
        """
        Use depth-first-search, iteratively

        Time: O(m * n) (we might visit every pixel once)
        Space: O(m * n) (the max size of the stack)
        """

        # if starting pixel is already new_color, flood fill would do nothing
        start_color = image[sr][sc]
        if start_color == new_color:
            return image

        R = len(image)
        C = len(image[0])

        # initiate DFS from starting pixel
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if image[r][c] == start_color:

                # update pixel color
                image[r][c] = new_color

                # add valid neighboring pixels to stack
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for neighbor in neighbors:
                    i, j = r + neighbor[0], c + neighbor[1]
                    if (
                        0 <= i < R
                        and 0 <= j < C
                        and image[i][j] == start_color
                    ):
                        stack.append((i, j))

        return image

    def flood_fill_recursive(
        self, image: list[list[int]], sr: int, sc: int, new_color: int
    ) -> list[list[int]]:
        """
        Use depth-first-search, recursively

        Time: O(m * n) (we might visit every pixel once)
        Space: O(m * n) (the max size of the call stack)
        """

        # if starting pixel is already new_color, flood fill would do nothing
        start_color = image[sr][sc]
        if start_color == new_color:
            return image

        R = len(image)
        C = len(image[0])

        def dfs(r, c):
            # initiate DFS from (r, c) if it matches the starting color
            if image[r][c] == start_color:

                # update pixel color
                image[r][c] = new_color

                # dfs on valid neighboring pixels
                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for neighbor in neighbors:
                    i, j = r + neighbor[0], c + neighbor[1]
                    if (
                        0 <= i < R
                        and 0 <= j < C
                        and image[i][j] == start_color
                    ):
                        dfs(i, j)

        dfs(sr, sc)
        return image


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2],
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ],
        [
            "Example 2",
            [[[0, 0, 0], [0, 0, 0]], 0, 0, 2],
            [[2, 2, 2], [2, 2, 2]],
        ],
        ["Small Inputs", [[[1], [1]], 0, 0, 2], [[2], [2]]],
        [
            "Large Inputs",
            [
                [
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                ],
                0,
                3,
                2,
            ],
            [
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 2],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
            ],
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
