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

        # TODO: I didn't think about the case in which the intervals don't 
        # overlap and the end of the current interval is less than the start
        # of my last merged interval. With this in mind, I realize that I need
        # to not only compare each interval to the last merged interval, but
        # in the above case, I then need to see if interval overlaps with ANY
        # of my merged intervals. Ugh. That's harder. Pausing for now.

        # check for empty or length 1 input
        if len(intervals) <= 1:
            return intervals

        # initiate new list to store merged intervals
        merged = [intervals[0]]

        # iterate over remaining intervals
        for interval in intervals[1:]:

            # if overlap with the last merged interval, then handle the merge
            if interval[0] <= merged[-1][1]:
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][1] = max(merged[-1][1], interval[1])

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
        ['Decreasing Start Interval', [[[1, 4], [0, 4]]], [[0, 4]]],
        ['Two Overlaps', [[[1, 3], [2, 6], [8, 10], [15, 18]]],
            [[1, 6], [8, 10], [15, 18]]],
        ['No Overlap, Not Sorted', [[[1, 4], [0, 0]]], [[0, 0], [1, 4]]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
