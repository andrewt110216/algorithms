from p0189_solution import Solution
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
        args = [[1, 2, 3, 4, 5, 6, 7], 3]
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[-1, -100, 3, 99], 2]
        expected = [3, 99, -1, -100]
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[1, 2, 3, 4], 0]
        expected = [1, 2, 3, 4]
        self.run_funcs(args, expected)

    def test4_single_element(self):
        args = [[1], 3]
        expected = [1]
        self.run_funcs(args, expected)

    def test5_k_larger_than_n(self):
        args = [[1, 2, 3, 4, 5], 12]
        expected = [4, 5, 1, 2, 3]
        self.run_funcs(args, expected)

    def test6_additional_Test(self):
        args = [[1, 2, 3, 4, 5, 6], 4]
        expected = [3, 4, 5, 6, 1, 2]
        self.run_funcs(args, expected)
