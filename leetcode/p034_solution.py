# 034 - Find First and Last Position of Element in Sorted Array
# leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:

    # list the methods to be run against the test cases
    implementations = ['find_first_and_last']

    def find_first_and_last(self, nums: list, target: int) -> list[int]:
        """
        Use a modified version of binary search

        When target is found, evaluate if it is the desired occurence (first or
        last) and update the binary search accordingly

        Time: O(log n) (binary search)
        Space: O(1)
        """

        # check for empty input
        if not nums:
            return [-1, -1]

        # find the index of the first occurence of target
        first_idx = self.find_bound(nums, target)

        # if first_idx is -1 then the target is not in nums
        if first_idx == -1:
            return [-1, -1]

        # find the index of the last occurence of target
        last_idx = self.find_bound(nums, target, first=False)

        return [first_idx, last_idx]

    def find_bound(self, nums, target, first=True):
        """Implement modified binary search to find first or last occurence"""

        # set pointers
        n = len(nums)
        start, end = 0, n
        mid = (start + end) // 2

        # use binary search algorithm to look for target
        while start <= end and mid in range(n):

            # if target is less than nums[mid], move our search to the left
            if target < nums[mid]:
                end = mid - 1

            # if target is greater than nums[mid], move our search to the right
            elif target > nums[mid]:
                start = mid + 1

            # if nums[mid] == target, determine if it is the right occurence
            else:

                # if we are looking for the first occurence
                if first:

                    # case 1: mid is the first occurence of target, meaning
                    # mid is start or the number to the left of mid != target
                    if mid == start or nums[mid - 1] != target:
                        return mid

                    # case 2: mid is not the first occurence of target
                    # move our search to the left of mid
                    else:
                        end = mid - 1

                # if nums[mid] == target and we are looking for last occurence
                else:

                    # case 1: mid is the last occurence of target, meaning
                    # mid is end, or the number to the right of mid != target
                    if mid in [end, n - 1] or nums[mid + 1] != target:
                        return mid

                    # case 2: mid is not the last occurence of target
                    # move our search to the right of mid
                    else:
                        start = mid + 1

            # reset mid for the next iteration
            mid = (start + end) // 2

        # target was not found
        return -1


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[5, 7, 7, 8, 8, 10], 8], [3, 4]],
        ['Example 2', [[5, 7, 7, 8, 8, 10], 6], [-1, -1]],
        ['Example 3', [[], 0], [-1, -1]],
        ['Many Targets - Start', [[-5, -5, -5, -1, 0, 0, 6, 100], -5], [0, 2]],
        ['Many Targets - End', [[0, 6, 100, 112, 112, 112, 112], 112], [3, 6]],
        ['Only Target - Length 2', [[2, 2], 2], [0, 1]],
        ['Only Target - Length 5', [[5, 5, 5, 5, 5], 5], [0, 4]],
        ['No Target - Length 2', [[2, 2], 3], [-1, -1]],
        ['Input Size 1', [[1], 1], [0, 0]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
