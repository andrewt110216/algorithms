# 001 - Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['two_sum']  # two_sum_brute is too slow for large input

    def two_sum(self, nums: list[list[int]], target: int) -> list[int]:
        """
        Dynamic programming, saving seen elements in a dictionary during the
        single pass through the list. The dictionary allows for O(1) lookup to
        see if we have already seen the complement to the current number.

        Time: O(n)
        Space: O(n)
        """

        # save seen elements in a dictionary (element value: element index)
        seen = {}

        # enumerate nums to access each element value and index
        for i, num in enumerate(nums):

            # calculate complement to current num and look for it in seen
            complement = target - num
            if complement in seen:

                # return indexes of current num and its complement
                return [seen[complement], i]

            # otherwise, add num to seen and move on to next element in nums
            else:
                seen[num] = i

        # no solution was found
        return False

    def two_sum_brute(self, nums: list[list[int]], target: int) -> list[int]:
        """
        Brute force, iterative solution, using nested for loop to evaluate
        every pair of elements in nums.

        Time: O(n^2) (n = 50,000 => runtime ~1 minute)
        Space: O(1)
        """

        n = len(nums)
        # iterate over all elements from first to 2nd-last
        for i in range(n-1):

            # iterate over all elements to the right of i
            for j in range(i + 1, n):

                # check if current pair (i, j) adds to target
                if nums[i] + nums[j] == target:
                    return [i, j]

        # no solution was found
        return False


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[2, 7, 11, 15], 9], [0, 1]],
        ['Example 2', [[3, 2, 4], 6], [1, 2]],
        ['Example 3', [[3, 3], 6], [0, 1]],
        ['Large Input', [list(range(10_001)), 19_999], [9_999, 10_000]],
        ['No Solution', [[1, 2, 3, 4, 5], 10], False],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
