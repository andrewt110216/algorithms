from p0198_solution import Solution
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
        args = [[1, 2, 3, 1]]
        expected = 4
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[2, 7, 9, 3, 1]]
        expected = 12
        self.run_funcs(args, expected)

    def test3_more_houses(self):
        args = [[2, 7, 9, 3, 1, 5, 4, 5]]
        expected = 21
        self.run_funcs(args, expected)

    def test4_increasing_order(self):
        args = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        expected = 64
        self.run_funcs(args, expected)

    def test5_complex(self):
        args = [[5, 10, 15, 22, 16, 24, 30, 14, 6, 4, 22]]
        expected = 94
        self.run_funcs(args, expected)
