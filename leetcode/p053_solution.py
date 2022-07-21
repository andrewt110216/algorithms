# 053 - Maximum Subbary
# https://leetcode.com/problems/maximum-subarray/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['max_subarray_sum']

    def max_subarray_sum(self, nums: list[int]) -> int:
        """
        Use dynamic programming to calculate the maximum sum ending at each
        element, and return the maximum local max

        Note that the max sum ending at i is either itself, or itself plus the
        maximum sum ending at i - 1 (if that sum is positive)

        Time: O(n) (one iteration through nums)
        Space: O(1) (constant space additional memory used)
        """

        # check for empty input
        if not nums:
            return 0

        # we need to track the max sum at i - 1 and the overall max
        prev_max = overall_max = nums[0]

        # start iterating over nums at the 2nd element
        for num in nums[1:]:

            # current sum is at least num
            cur_sum = num

            # if max subarray sum through i - 1 > 0, add it to the current sum
            if prev_max > 0:
                cur_sum += prev_max

            # update overall and previous maximum sums for next iteration
            overall_max = max(overall_max, cur_sum)
            prev_max = cur_sum

        return overall_max


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 6],
        ['Example 2', [[1]], 1],
        ['Example 3', [[5, 4, -1, 7, 8]], 23],
        ['Empty Input', [[]], 0],
        ['Large Input', [list(range(100_000))], sum(range(100_000))],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
