from leetcode.p0347_solution import Solution
import copy


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

            # order of ouput does not matter
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()

            assert result == expected

    def test1_example1(self):
        args = [[1, 1, 1, 2, 2, 3], 2]
        expected = [1, 2]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[1], 1]
        expected = [1]
        self.run_funcs(args, expected)

    def test3_larger_input(self):
        args = [[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5], 5]
        expected = [1, 2, 3, 4, 5]
        self.run_funcs(args, expected)

    def test4_complex_input(self):
        args = [[1, 2, 1, 4, 5, 1, 4, 6, 1, 7, 7, 8, 2, 2, 2, 2, 2, 1, 4], 3]
        expected = [4, 1, 2]
        self.run_funcs(args, expected)
