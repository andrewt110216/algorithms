# 198 - House Robber
# https://leetcode.com/problems/house-robber/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["rob_houses"]

    def rob_houses(self, nums: list[int]) -> int:
        """
        Use dynamic programming, updating nums in-place

        At each home, the maximum amount that can be stolen up to and including
        that home is equal to the max of:

        1) the max from two homes ago + the money in the current home OR
        2) the max from the prior home

        Iterate over each home, calculating the maximum amount of money that
        can be stolen up to and including that home, and update nums in place.

        Since the max bounty is non-descending, the max bounty through the
        final house is the desired result.

        Time: O(n) (one pass through nums)
        Space: O(1) (no additional data structures used)
        """

        n = len(nums)

        # handle case with single house
        if n == 1:
            return nums[0]

        # calculate max bounty through the second house, which is just the max
        # of the bounty in the first two houses (since only 1 can be robbed)
        nums[1] = max(nums[0], nums[1])

        # iterate over remaining houses, calculating max bounty
        for i in range(2, n):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])

        return nums[-1]


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[1, 2, 3, 1]], 4],
        ["Example 2", [[2, 7, 9, 3, 1]], 12],
        ["More Houses", [[2, 7, 9, 3, 1, 5, 4, 5]], 21],
        [
            "Increasing Order",
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
            64,
        ],
        ["Complex", [[5, 10, 15, 22, 16, 24, 30, 14, 6, 4, 22]], 94],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
