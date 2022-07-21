# 056 - Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['merge_intervals']

    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Iterate over the intervals and evalute whether or not each interval
        can be merged into the last merged interval, or if it starts a new
        merged interval

        Time: O(n) (iterate over intervals once)
        Space: O(n) (max length of new list of merged intervals)
        """

        # check for empty or length 1 input
        if len(intervals) <= 1:
            return intervals

        # initiate new list to store merged intervals
        merged = [intervals[0]]

        # iterate over remaining intervals
        for interval in intervals[1:]:

            # if overlap with the last merged interval, then merge
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = interval[1]

            # if no overlap with the last merged interval, append to merged
            else:
                merged.append(interval)

        return merged


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [[[1, 3], [2, 6], [8, 10], [15, 18]]],
            [[1, 6], [8, 10], [15, 18]]],
        ['Example 2', [[[1, 4], [4, 5]]], [[1, 5]]],
        ['One Interval', [[[1, 5]]], [[1, 5]]],
        ['No Overlap', [[[1, 3], [5, 7], [8, 10]]], [[1, 3], [5, 7], [8, 10]]],
        ['All Overlap', [[[1, 3], [2, 4], [3, 5]]], [[1, 5]]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
