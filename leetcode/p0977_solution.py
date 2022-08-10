# 977 - Squares of Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["get_sorted_squares"]

    def get_sorted_squares(self, nums: list) -> list:
        """
        Use two pointers to calculate the squares and sort in one pass

        Since nums is already sorted in non-decreasing order, the only concern
        we have in sorting is when there exist negative numbers in nums. By
        using a pointer starting from each end of nums, we can calculate the
        squares of each end number, and fill in the sorted squares list from
        right to left by taking the larger square each time.

        Time: O(n)
        Space: O(n) (the output list)
        """

        # set up pointers
        n = len(nums)
        left = 0
        right = n - 1

        # set up output list so we can add squares to it in reverse order
        sorted_squares = [0] * n

        # Iterate result in reverse, since by incrementing from the ends,
        # we are moving in descending order (in absolute values)

        # i represents the index in sorted_squares
        # we will fill it from right to left, adding the largest squares first
        for i in range(n - 1, -1, -1):
            a, b = nums[left], nums[right]
            if abs(a) > abs(b):
                sorted_squares[i] = a * a
                left += 1
            else:
                sorted_squares[i] = b * b
                right -= 1

        return sorted_squares


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[1, 3, 7, 10, 12, 15]], [1, 9, 49, 100, 144, 225]],
        ["Example 2", [[-7, -3, 2, 3, 11]], [4, 9, 9, 49, 121]],
        ["Single Element - Positive", [[3]], [9]],
        ["Single Element - Negative", [[-3]], [9]],
        ["Two Elements", [[-1, 5]], [1, 25]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
