from leetcode.p0077_solution import Solution
from itertools import combinations


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)

            # order does not matter for this output
            # if result is list, sort it and expected result for comparison
            for var in [result, expected]:
                if type(var) in [list, tuple]:
                    var.sort()
                    if type(var[0]) in [list, tuple]:
                        [x.sort() for x in var]

            assert result == expected

    def test1_example1(self):
        args = [4, 2]
        expected = [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [1, 1]
        expected = [[1]]
        self.run_funcs(args, expected)

    def test3_large_output(self):
        args = [10, 3]
        expected = list(combinations(range(1, 11), 3))

        # need to convert combinations from itertools.combinations
        # from tuples to lists, for comparison against our function result
        for i in range(len(expected)):
            expected[i] = list(expected[i])

        self.run_funcs(args, expected)
