# 46 - Permuatations
# https://leetcode.com/problems/permutations/NK

from itertools import permutations


class Solution:

    # list the methods to be run against the test cases
    implementations = ["permutations"]

    def permutations(self, nums: list[int]) -> list[list[int]]:
        """
        Use backtracking

        Time: O( SUM, k=1 to n, OF: ( n! / (n - k)!) )
         - for each k from 1 to n, we look at all k-permutations of n
        Space: O( n! ) (the call stack equal to number of permutations)
        """

        def recurse(first):
            if first == n:
                output.append(nums[:])
            else:
                for i in range(first, n):
                    # swap first and i
                    nums[i], nums[first] = nums[first], nums[i]
                    # recurse starting with next element
                    recurse(first + 1)
                    # backtrack (reverse swap)
                    nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        output = []
        recurse(0)
        return output


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [[1, 2, 3]],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ],
        [
            "Example 2",
            [[0, 1]],
            [[0, 1], [1, 0]],
        ],
        [
            "Example 3",
            [[1]],
            [[1]],
        ],
        [
            "Large Input",
            [[1, 2, 3, 4, 5, 6]],
            list(permutations(range(1, 7), 6)),
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases, ordered_d1=False, ordered_d2=True)
    pt.run()
