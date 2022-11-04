# MergeSort
# Sorts an array in-place by recursively sorting each half then merging them

# Analysis
#  Case     TC        SC    Comments
#  ----     --        --    ------
#  Worst    O(nlogn)  O(n)
#  Average  O(nlogn)  O(n)
#  Best     O(nlogn)  O(n)

# Stable
# Yes


def merge_sort(nums):
    """Sort nums in-place"""

    def _merge_sort(start, end):
        """Helper function for recursion"""

        # Base Case
        if start >= end:
            return

        mid = (start + end) // 2

        # Sort left and right halves
        _merge_sort(start, mid)
        _merge_sort(mid + 1, end)

        # Merge sorted subarrays
        _merge(start, mid + 1, end)

    def _merge(start1, start2, end):
        """Merges two sorted subarrays in-place"""

        # A copy of the original values is needed to update nums in-place
        original_nums = nums[start1 : end + 1]

        # Set up pointers for two parts of original_nums and merged result
        p1, p2 = 0, start2 - start1
        cur = start1

        # Copy smaller of p1 vs. p2 while both are in bounds
        while p1 < start2 - start1 and p2 <= end - start1:

            if original_nums[p1] <= original_nums[p2]:
                # Choosing from left side in case of tie maintains stable sorting
                nums[cur] = original_nums[p1]
                p1 += 1
            else:
                nums[cur] = original_nums[p2]
                p2 += 1
            cur += 1

        # Copy residual from p1 or p2
        while p1 < start2 - start1:
            nums[cur] = original_nums[p1]
            p1 += 1
            cur += 1
        while p2 <= end - start1:
            nums[cur] = original_nums[p2]
            p2 += 1
            cur += 1

    # Initial recursive call
    _merge_sort(0, len(nums) - 1)


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
        merge_sort(nums)
        print(nums)
