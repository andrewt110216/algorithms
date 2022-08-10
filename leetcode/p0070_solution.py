# 070 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


class Solution:

    # list the methods to be run against the test cases
    implementations = [
        "climb_stairs_fib_iterative",
        "climb_stairs_fib_recursive",
        "climb_stairs_memoization",
        "climb_stairs_brute_force",
    ]

    def climb_stairs_fib_recursive(self, n: int) -> int:
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

        Time: O( 2^n ) (at each i up to n, 2 recursive calls are made)
        Space: O( 2^n ) (max size of call stack)
        """

        if n == 1:
            return 1
        if n == 2:
            return 2

        a = self.climb_stairs_fib_recursive(n - 1)
        b = self.climb_stairs_fib_recursive(n - 2)
        return a + b

    def climb_stairs_fib_iterative(self, n: int) -> int:
        """
        The solution represents the (n-1)th Fibonacci number.
        Use an iterative solution.

        Time: O(n) (a calculation is made for each number from 1 to n)
        Space: O(1) (constant space is used)
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

    def climb_stairs_memoization(self, n: int) -> int:
        """
        Use memoization to reduce the number of recursive calls, so that only
        one recursive call is made per step

        Time: O(n) (depth of the call stack)
        Space: O(n) (depth of the call stack)
        """

        def take_a_step(i, n, memo):
            if i == n:
                # if we reach the nth step, the path was successful
                return 1
            elif i > n:
                # if we past the nth step, the path was unsuccessful
                return 0
            elif memo[i] > 0:
                return memo[i]
            # we aren't to n yet. Try taking 1 step and try 2 steps
            memo[i] = take_a_step(i + 1, n, memo) + take_a_step(i + 2, n, memo)
            return memo[i]

        # store count of completed paths in list so recursive calls can access
        memo = [0] * n
        return take_a_step(0, n, memo)

    def climb_stairs_brute_force(self, n: int) -> int:
        """
        At each step, initate a recursive call that takes 1 step and another
        call that takes 2 steps. If we reach n, then add 1 to the count of
        possible ways. Otherwise, add 0 as the path was invalid.

        Time: O(2^n) (we take 2 steps at each integer from 1 to n)
        Space: O(n) (depth of the call stack)
        """

        def take_a_step(steps=0):
            if steps == n:
                # if we reach the nth step, the path was successful
                result[0] += 1
            elif steps > n:
                # if we past the nth step, the path was unsuccessful
                return
            else:
                # we aren't to n yet. Try taking 1 step and try 2 steps
                take_a_step(steps + 1)
                take_a_step(steps + 2)

        # store count of completed paths in list so recursive calls can access
        result = [0]
        take_a_step(0)
        return result[0]


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
        # recursive and brute force solutions are too slow for n > 30
        # ["Larger Input", [40], 165_580_141],
        # ["Largest Input", [45], 1_836_311_903],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
