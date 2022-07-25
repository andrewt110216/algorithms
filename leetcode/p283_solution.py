# 283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['move_zeroes_swaps', 'move_zeroes_shifts']

    def move_zeroes_swaps(self, nums: list[int]) -> list[int]:
        """
        Use two pointers

        The goal is to move all 0's to the end of nums, in-place.
        We can also think of this as moving non-zero elements to the front
        of nums, maintaining their relative order.

        We will traverse nums, and swap any non-zero elements to the front
        of the list, which will result in the zeroes being moved to the end.

        We simply need to create a second pointer that designates the next
        index at which to place a non-zero, and increment this after each swap

        Time: O(n) (we traverse nums once)
        Space: O(1) (constant additional space is used)
        """

        # create pointer for where to place the next non-zero number
        next_non_zero = 0

        # iterate over nums, looking for non-zero numbers
        for i, num in enumerate(nums):

            # we don't need to swap if i equals next_non_zero
            if num != 0:

                # swap elements at indexes i and next_non_zero
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]

                # increment next non-zero pointer
                next_non_zero += 1

        return nums

    def move_zeroes_shifts(self, nums: list[int]) -> list[int]:
        """
        Use two pointers

        First, iterate over nums moving all non-zeroes to the front by using
        a pointer for where to place the next non-zero

        Then, fill in the remaining elements of nums with 0's

        Time: O(n) (at most we traverse nums twice, but O(2n) = O(n) )
        Space: O(1) (constant additional space is used)
        """

        # create pointer for where to place the next non-zero number
        next_non_zero = 0

        # iterate over nums, looking for non-zero numbers
        for i, num in enumerate(nums):

            # we don't need to shift if i equals next_non_zero
            if num != 0:

                # move element at indexe i to next_non_zero
                nums[next_non_zero] = nums[i]

                # increment next non-zero pointer
                next_non_zero += 1

        # now place 0's at each index after the last non-zero
        for i in range(next_non_zero, len(nums)):
            nums[i] = 0

        return nums


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]],
        ['Example 2', [[0]], [0]],
        ['No Zeroes', [[1, 2, 3, 4]], [1, 2, 3, 4]],
        ['All Zeroes', [[0, 0, 0, 0, 0]], [0, 0, 0, 0, 0]],
        ['Many Zeroes', [[0, 0, 0, 0, 1]], [1, 0, 0, 0, 0]],
        ['Longer, Complicated', [[0, 1, 2, 0, 4, 0, 5, 6, 7, 8, 9, 0, 10]],
            [1, 2, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
