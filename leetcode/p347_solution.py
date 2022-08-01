# 347 - Top K Frequent Items
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq


class Solution:

    # list the methods to be run against the test cases
    implementations = ["heap_sort", "bucket_sort", "count_and_sort"]

    def heap_sort(self, nums: list[int], k: int) -> list[int]:
        """
        Create a counter object of the frequencies of each number in nums.

        Create a heap of size k, and push/pop to the heap as new frequencies
        are greater than the current root of the heap.

        When finished, the heap will contain the k-most frequent numbers.

        Time: O(n * logk) (sorting of the heap)
        Space: O(n) (counter and heap data structures)
        """

        # if k == len(nums), then nums is already the output we need
        if k == len(nums):
            return nums

        # use Counter object to get frequencies of numbers in nums
        freqs = list(Counter(nums).items())

        # populate heap with the first k items
        heap = [(freq, num) for num, freq in freqs[:k]]
        heapq.heapify(heap)

        # consider remaining items and add to heap if would be in k-largest
        for num, freq in freqs[k:]:
            if freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, num))

        # the heap now continues the k most frequent numbers. extract numbers
        out = []
        for freq, num in heap:
            out.append(num)

        return out

    def bucket_sort(self, nums: list[int], k: int) -> list[int]:
        """
        Iterate over nums, counting the frequency of each number using a
        dictionary with nums -> frequency.

        Then create a list of empty lists, where each sublist represents all
        nums with frequency == index of list - 1. For example,
        [1, 1, 2, 2, 2, 3, 3] would produce d = {1: 2, 2: 3, 3: 2}, which would
        create buckets: [[], [1, 3], [2]].

        Then, flatten the list of buckets (since we are guaranteed a unique
        solution), and take the last k elements in the flattened list.

        Time: O(n) (all operations have max runtime of O(n) )
        Space: O(n) (space of dictionary and buckets)
        """

        # use Counter object to get frequencies of numbers in nums
        counts = Counter(nums).items()

        # populate the buckets of nums/frequencies
        # bucket[3] = [1, 2] => 1 and 2 both have frequency 4 in nums
        buckets = [[] for _ in nums]
        for num, freq in counts:
            buckets[freq - 1].append(num)

        # grab the top k frequency numbers from buckets
        out = []
        count = 0
        for bucket in buckets[::-1]:
            for x in bucket:
                out.append(x)
                count += 1
                if count == k:
                    return out

    def count_and_sort(self, nums: list[int], k: int) -> list[int]:
        """
        Iterate over nums, using a dictionary to store the frequencies of each
        number (O(n)).

        Sort the items of the dictionary by their frequency, and return the
        top k keys (O(n * log n).

        Time: O(n * log n) (sorting of keys)
        Space: O(n) (size of dictionary)
        """

        d = {}  # integer: count in nums
        for num in nums:
            d[num] = d.get(num, 0) + 1
        counts = list(d.items())
        counts.sort(key=lambda tup: tup[1], reverse=True)
        out = []
        for i in range(k):
            out.append(counts[i][0])
        return out


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[1, 1, 1, 2, 2, 3], 2], [1, 2]],
        ["Example 2", [[1], 1], [1]],
        [
            "Larger Input",
            [[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], 5],
            [1, 2, 3, 4, 5],
        ],
        [
            "Complex Input",
            [[1, 2, 3, 1, 4, 5, 1, 4, 6, 1, 7, 7, 8, 2, 2, 2, 2, 2, 1, 4], 3],
            [2, 1, 4],
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases, ordered_d1=False)
    pt.run()
