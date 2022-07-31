# 1006 - Clumsy Factorial
# https://leetcode.com/problems/clumsy-factorial/

from collections import deque


class Solution:

    # list the methods to be run against the test cases
    implementations = ["clumsy_factorial", "clumsy_factorial_v1"]

    def clumsy_factorial(self, n: int) -> int:
        """
        Iterate over each integer from n down to 1, updating the result as
        we go.

        Order of operations require that when we encounter a * b / c, we
        compute that complete expression before adding (or subtracting) to the
        result, so we will save that in a temporary variable. The very first
        time we encounter this expression ( n * (n - 1) / (n - 2) ), we are
        adding to the result. Every subsequent time, we are subtracting this
        expression from the result (e.g. " - (n - 4) * (n - 5) / (n - 6) ").

        Time: O(n) (iterate over each integer from n down to 1)
        Space: O(1) (constant additional space)
        """

        result = 0
        temp = n
        op = 0  # Operations: {0: *, 1: //, 2: +, 3: -}
        sign = 1
        for i in range(n - 1, 0, -1):
            if op == 0:
                temp *= i
            elif op == 1:
                temp //= i
                result += temp * sign
            elif op == 2:
                result += i
            else:  # op == 3:
                sign = -1
                temp = i
            op = (op + 1) % 4

        if op <= 1:
            result += temp * sign

        return result

    def clumsy_factorial_v1(self, n: int) -> int:
        """
        Use a stack to move through the integers from n down to 1, saving
        results for addition and subtraction in a separate queue.
        After processing the entire stack, then process the queue.

        This was my initial solution, which can be optimized in several ways.

        Time: O(n) (iterate through the stack, then again through the queue)
        Space: O(n) (stack and queue)
        """

        # first solution - can be optimized

        stack = deque(list(range(1, n+1)))
        add_sub = deque()
        op = 0

        # complete all multiplication, addition, division first
        # ops: (0, *), (1, //), (2, +)
        while len(stack) > 1:
            a = stack.pop()
            if op == 0:
                b = stack.pop()
                stack.append(a * b)
            elif op == 1:
                b = stack.pop()
                add_sub.append(a // b)
            elif op == 2:
                add_sub.append(a)
            op = (op + 1) % 3

        # move last item in stack to end of subtraction q
        if stack:
            add_sub.append(stack.pop())

        # complete the addition/subtraction calculations, if any
        add = True
        if add_sub:
            result = add_sub.popleft()
        while add_sub:
            a = add_sub.popleft()
            if add:
                result += a
            else:
                result -= a
            add = not add

        return result


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [4], 7],
        ["Example 2", [10], 12],
        ["Odd Number", [5], 7],
        ["Larger Number", [21], 23],
        ["Larger Number 2", [99], 98],
        ["Largest Number", [1_000], 1_001],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
