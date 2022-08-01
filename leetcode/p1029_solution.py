# 1029 - Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["calculate_cost"]

    def calculate_cost(self, costs: list[list[int]]) -> int:
        """
        In order to minimize costs, the people with the highest differential
        costs between the two cities should be assigned first. Calculate the
        differential as di = aCosti - bCosti, then sort costs by di.

        Assign the first n people to city A, and remaining to city B.

        Time: O(nlogn) (sorting)
        Space: O(1) (sorting done in place, so no new data structures)
        """

        n = len(costs) // 2

        # sort costs based on differential
        costs.sort(key=lambda person: person[0] - person[1])

        # assign first n people to city A, next n to city B
        total_cost = 0
        for i in range(n):
            total_cost += costs[i][0] + costs[i + n][1]

        return total_cost


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [[[10, 20], [30, 200], [400, 50], [30, 20]]], 110],
        [
            "Example 2",
            [
                [
                    [259, 770],
                    [448, 54],
                    [926, 667],
                    [184, 139],
                    [840, 118],
                    [577, 469],
                ]
            ],
            1859,
        ],
        [
            "Example 3",
            [
                [
                    [515, 563],
                    [451, 713],
                    [537, 709],
                    [343, 819],
                    [855, 779],
                    [457, 60],
                    [650, 359],
                    [631, 42],
                ]
            ],
            3086,
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
