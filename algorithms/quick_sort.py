# Randomized QuickSort
# Sorts an array in-place by recursively partitioning around a pivot element

# Time Complexity
#  Case           TC          Comments
#  ----           --          --------
#  Worst          O(n^2)      Partitions are always smallest or greatest vals
#  Average        O(nlogn)    Average partition lands in middle 50%
#  Best           O(nlogn)

# Space Complexity
# O(1)

# Stable
# No

import random


def quick_sort(nums):
    """Sort nums in-place"""

    def _quick_sort(start, end):
        """Helper function for recursion"""

        # Base Case
        if start >= end:
            return

        k = partition(start, end)

        # Recurse on left part of partition
        _quick_sort(start, k - 1)

        # Recurse on right part of partition
        _quick_sort(k + 1, end)

    def partition(start, end):
        """Partition nums from start to end around a random pivot and return the pivot index"""

        # Choose a pivot index at random and swap it into start index
        pivot_idx = random.randint(start, end)
        pivot = nums[pivot_idx]
        nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]

        # Swap all values less than pivot to front
        swap_index = start + 1
        for cur in range(start + 1, end + 1):
            if nums[cur] < pivot:
                nums[swap_index], nums[cur] = nums[cur], nums[swap_index]
                swap_index += 1

        # Swap pivot from start to the partitioned index
        nums[start], nums[swap_index - 1] = nums[swap_index - 1], nums[start]

        # Return partition index
        return swap_index - 1

    # Initial recursive call
    _quick_sort(0, len(nums) - 1)


if __name__ == "__main__":

    test_inputs = [
        [3, 8, 2, 5, 1, 4, 7, 6],
        [-2, 3, 8, 2, -5, 12, 5, 1, 4, -7, 6, 0, 15, 7, 14, 13, -4],
        [1, 5, 2, 2, 4, 1, 1, 6, 5, 5, 5, 2],
        [3, 1],
        [7],
        [],
    ]

    for nums in test_inputs:
        quick_sort(nums)
        print(nums)
