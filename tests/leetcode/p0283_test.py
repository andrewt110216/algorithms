from leetcode.p0283_solution import Solution
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

            assert result == expected

    def test1_example1(self):
        args = [[0, 1, 0, 3, 12]]
        expected = [1, 3, 12, 0, 0]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[0]]
        expected = [0]
        self.run_funcs(args, expected)

    def test3_no_zeroes(self):
        args = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.run_funcs(args, expected)

    def test4_all_zeroes(self):
        args = [[0, 0, 0, 0, 0]]
        expected = [0, 0, 0, 0, 0]
        self.run_funcs(args, expected)

    def test5_many_zeroes(self):
        args = [[0, 0, 0, 0, 1]]
        expected = [1, 0, 0, 0, 0]
        self.run_funcs(args, expected)

    def test6_longer_and_complicated(self):
        args = [[0, 1, 2, 0, 4, 0, 5, 6, 7, 8, 9, 0, 10]]
        expected = [1, 2, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0]
        self.run_funcs(args, expected)
