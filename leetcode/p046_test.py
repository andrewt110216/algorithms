from p046_solution import Solution
import copy
from itertools import permutations


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)

            # use a deep copy of args so side effects on pass-by-reference
            # variables do not persist for subsequent implementations
            args_copy = copy.deepcopy(args)
            result = func(*args_copy)

            # order does not matter for this output
            # if result is list, sort it and expected result for comparison
            for var in [result, expected]:
                if type(var) in [list, tuple]:
                    var.sort()
                    if type(var[0]) in [list, tuple]:
                        [x.sort() for x in var]

            assert result == expected

    def test1_example1(self):
        args = [[1, 2, 3]]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
                    [3, 2, 1]]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[0, 1]]
        expected = [[0, 1], [1, 0]]
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[1]]
        expected = [[1]]
        self.run_funcs(args, expected)

    def test4_large_input(self):
        args = [[1, 2, 3, 4, 5, 6]]
        expected = list(permutations(range(1, 7), 6))

        # need to convert combinations from itertools.combinations
        # from tuples to lists, for comparison against our function result
        for i in range(len(expected)):
            expected[i] = list(expected[i])

        self.run_funcs(args, expected)
