# 189 - Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['rotate_cyclical', 'rotate_new']

    def rotate_cyclical(self, nums: list[int], k: int) -> list[int]:
        """
        Cyclical replacements

        Swap index i with index i + k, saving the value from index i + k in a
        temporary variable. Then, copy the temporary value into (i + k) + k,
        wrapping around to the beginning of nums, using remainder division.

        In the case that n is a factor of k, we would iterate over the same
        elements on each pass through nums. In this case, offset the starting
        position by 1 on each pass through nums.

        Continue swapping in this manner until exactly n swaps are completed,
        so that every element is swapped into the correct position

        Time: O(n) (each element is visited exactly once)
        Space: O(1) (constant additional space is used)
        """

        # reduce k by eliminating redundant rotations
        n = len(nums)
        k %= n

        # return if no rotations needed
        if k == 0:
            return nums

        # swap elements exactly n times
        start = 0
        swaps = 0
        while swaps < n:
            i = start
            temp = nums[i]
            while True:
                j = (i + k) % n
                nums[j], temp = temp, nums[j]
                swaps += 1
                i = j
                if i == start:
                    start += 1
                    break

        return nums

    def rotate_new(self, nums: list[int], k: int) -> list[int]:
        """
        Iterate over nums and copy each value at index i to index i + k of a
        new array. Then, copy the new array back into nums

        Time: O(n) (one pass over nums)
        Space: O(n) (temporary new array used)
        """

        # reduce k by eliminating redundant rotations
        n = len(nums)
        k %= n
        result = [0] * n

        # copy each element from nums into result
        for i in range(n):
            j = (i + k) % n
            result[j] = nums[i]

        # copy result into nums
        for i in range(n):
            nums[i] = result[i]

        return nums


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[1, 2, 3, 4, 5, 6, 7], 3], [5, 6, 7, 1, 2, 3, 4]],
        ['Example 2', [[-1, -100, 3, 99], 2], [3, 99, -1, -100]],
        ['No Rotations', [[1, 2, 3, 4], 0], [1, 2, 3, 4]],
        ['Single Element', [[1], 3], [1]],
        ['K Larger Than N', [[1, 2, 3, 4, 5], 12], [4, 5, 1, 2, 3]],
        ['Additional Test', [[1, 2, 3, 4, 5, 6], 4], [3, 4, 5, 6, 1, 2]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
