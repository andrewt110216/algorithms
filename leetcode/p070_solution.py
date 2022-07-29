# 070 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


class Solution:

    # list the methods to be run against the test cases
    # climb_stairs_recursive is too slow for n > 30
    implementations = ["climb_stairs_iterative"]

    def climb_stairs_recursive(self, n: int) -> int:
        """
        Observe the pattern as n increases:

        Base Case: n = 1 => 1 ([1])
        When n = 2 => 2 ([1, 1], [2])
        When n = 3 => 3 ([1, 1, 1], [1, 2], [2, 1])
        When n = 4 => 5 ([1, 1, 1, 1], [2, 1, 1], [2, 2], [1, 2, 1], [1, 1, 2])
        When n = 5 => 8 ([1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [2, 1, 2],
                         [1, 2, 1, 1], [1, 2, 2], [1, 1, 2, 1], [1, 1, 1, 2])

        The solution represents the (n-1)th Fibonacci number!
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]
         => f(n) = f(n - 1) + f(n - 2)

        We will use recursion to calculate the solution.

        Time: O()
        Space: O()
        """

        if n == 1:
            return 1
        if n == 2:
            return 2

        a = self.climb_stairs_recursive(n - 1)
        b = self.climb_stairs_recursive(n - 2)
        return a + b

    def climb_stairs_iterative(self, n: int) -> int:
        """
        The solution represents the (n-1)th Fibonacci number.
        Use an iterative solution.

        Time: O()
        Space: O()
        """

        # handle base cases
        if n <= 2:
            return n

        # set the current and prior fibonacci numbers
        i = 2
        prev, cur = 1, 2

        # calculate next fibonacci number until i == n
        while i < n:
            cur, prev = cur + prev, cur
            i += 1

        return cur


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [2], 2],
        ["Example 2", [3], 3],
        ["Smallest Input", [1], 1],
        ["Medium Input", [5], 8],
        ["Large Input", [30], 1_346_269],
        ["Larger Input", [40], 165_580_141],
        ["Largest Input", [45], 1_836_311_903],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
