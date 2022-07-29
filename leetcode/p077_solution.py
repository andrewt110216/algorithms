# 077 - Combinations
# https://leetcode.com/problems/combinations/

from itertools import combinations


class Solution:

    # list the methods to be run against the test cases
    implementations = ["get_combinations"]

    def get_combinations(self, n: int, k: int) -> list[list[int]]:
        """
        Use backtracking

        Time: O(n choose k) (each combination is generated exactly once)
        Space: O(n choose k) (the size of the call stack)
        """

        def recurse(start, cur_combo=[]):

            # check if the current combination is complete (i.e. has length k)
            if len(cur_combo) == k:
                combinations.append(cur_combo[:])  # use a copy of cur_combo
                return  # prevent cur_combo to continue growing past length k

            # iterate over the intergers from start to n
            for i in range(start, n + 1):

                # add i to the current combination
                cur_combo.append(i)

                # recurse  with i + 1 to complete the combination
                recurse(i + 1, cur_combo=cur_combo)

                # a current combination was completed and added to combinations
                # so remove the first element and continue
                cur_combo.pop()

        combinations = []
        recurse(1)
        return combinations


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [4, 2],
            [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]],
        ],
        ["Example 2", [1, 1], [[1]]],
        ["Large Output", [10, 3], list(combinations(range(1, 11), 3))],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases, ordered_d1=False, ordered_d2=False)
    pt.run()
