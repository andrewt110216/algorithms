# NUM - NAME
# LINK


class Solution:

    # list the methods to be run against the test cases
    implementations = ["binary_search"]

    def binary_search(self, nums: list[int], target: int) -> int:
        """
        Implement the binary search algorithm

        Use two pointers, left & right, beginning at 0 and (n-1), respectively.
        1. Take the number in the middle of left & right, mid.
        2. Compare mid to the target number:
         - if we guessed right, and mid == target, return the index of mid
         - if mid > target, then we know that target must be to the left of mid
           if it exists at all. So, set 'right = mid - 1' and go back to step 1
         - if mid < target, then set 'left = mid + 1' and go back to step 1

        If at any point left becomes greater than right, that means that target
        cannot exist in nums. More explicitly, it means that we found adjacent
        elements, say at indexes i and i + 1, such that:
            nums[i] < target < nums[i + 1]
        Since nums is sorted in ascending order, target cannot be in nums.

        Time: O(log n)
         - After each iteration in the while loop, our range [left:right] is
           halved. In the worst case that target exists where left = right, we
           have divided the length of nums by 2 until we have 1 remaining.
           This is exactly log(2)n (log base 2 of n). Since changing base of
           a logarithm is a constant factor, the base is not relevant in Big O
        Space: O(1) (constant additional space is used)
        """

        # initialize pointers
        left = 0
        right = len(nums) - 1

        # begin binary search
        while left <= right:

            # calculate the midpoint of right & left using floor division
            mid = (right + left) // 2
            num = nums[mid]

            # compare num to target to determine next step
            if num == target:
                return mid
            elif target < num:
                right = mid - 1
            else:  # target > num
                left = mid + 1

        # target doesn't exist in nums
        return -1


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[-1, 0, 3, 5, 9, 12], 9], 4],
        ["Example 2", [[-1, 0, 3, 5, 9, 12], 2], -1],
        ["Length 1 - Match", [[1], 1], 0],
        ["Length 1 - No Match", [[1], 2], -1],
        ["Target at End - Even", [[1, 2, 3, 4, 5, 6], 6], 5],
        ["Target at End - Odd", [[1, 2, 3, 4, 5, 6, 7], 7], 6],
        ["Target at Start - Even", [[1, 2, 3, 4, 5, 6], 1], 0],
        ["Target at Start - Odd", [[1, 2, 3, 4, 5, 6, 7], 1], 0],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
