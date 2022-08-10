# 215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from random import randint


class Solution:

    # list the methods to be run against the test cases
    implementations = ["find_kth_largest"]

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        """
        Use a variation on QuickSort, called QuickSelect

        For simplicity, we will sort the list in non-descending order.
        So, instead of the kth largest element, we will search for the element
        at index (n-k) of the list sorted in non-descending order.
        We will immediately set k = n - k.

        When completing the partition subroutine, note that the pivot element
        is placed in its correct sorted order. Let that be the jth element.
        Then, if k is less than j, we know that the kth largest element must
        lie to the left of j, and vice versa if k larger than j.

        We only need to continue on the portion containing k, and we proceed
        until it is found.

        Time: O(n) (Master Theorem: a=1, b=2, d=1 => CASE 2)
        Space: O(1) (sorted in place)
        """

        # index (n-k) in non-descending order is same as kth largest
        n = len(nums)
        k = n - k

        # helper function: partition subroutine
        def partition(pivot_idx, left, right):
            """Partition nums[left:right] (inclusive) around pivot element"""

            # save the value of the pivot element
            pivot = nums[pivot_idx]

            # swap the pivot element into the left index
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]

            # i delineates the partition of elements less than pivot
            # all values to the left of i are less than or equal to pivot
            i = left + 1

            # iterate over each element to be partitioned [left + 1 to right]
            for j in range(left + 1, right + 1):

                # if nums[j] is less than or equal to pivot, swap it with
                # index i and increment i. This enforces our partition that all
                # values <= pivot lie to the left of i
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            # the final step is to place the pivot element in the correct index
            # index i - 1 is the last value less than or equal to the pivot,
            # so we will swap the pivot with index i - 1
            nums[i - 1], nums[left] = nums[left], nums[i - 1]

            # return the final index of the pivot element
            return i - 1

        # main recursive function
        def quickselect(left, right):
            """Modified quicksort on nums to find the (k-1)th smallest value"""

            # base case, range of length 1 cannot be partitioned
            if left == right:
                return nums[left]

            # random choice of the pivot element optimizes the algorithm
            pivot = randint(left, right)

            # partition nums around pivot and get its final position, q
            q = partition(pivot, left, right)

            # compare q to k to determine the next step
            if q == k:

                # the pivot turned out to be the kth element
                return nums[q]

            # k lies to the left of q
            elif k < q:

                # recurse to the left of q
                return quickselect(left, q - 1)

            # k lies to the right of q
            else:

                # recurse to the right of q
                return quickselect(q + 1, right)

        return quickselect(0, n - 1)


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[3, 2, 1, 5, 6, 4], 2], 5],
        ["Example 2", [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], 4],
        ["Length 1", [[5], 1], 5],
        ["Length 2", [[5, 4], 2], 4],
        [
            "Add Negatives, Zeroes, Duplicates",
            [[-7, 9, -5, 0, 3, 9, -5, -1, 10, 8, 6, -1], 9],
            -1,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
