from p286_solution import Solution
import copy


class TestClass:

    s = Solution()
    inf = 2147483647

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
        args = [
            [
                [self.inf, -1, 0, self.inf],
                [self.inf, self.inf, self.inf, -1],
                [self.inf, -1, self.inf, -1],
                [0, -1, self.inf, self.inf],
            ]
        ]
        expected = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[-1]]]
        expected = [[-1]]
        self.run_funcs(args, expected)

    def test3_larger_grid(self):
        args = [
            [
                [0, self.inf, self.inf, -1, self.inf, self.inf],
                [-1, self.inf, self.inf, -1, -1, 0],
                [-1, self.inf, self.inf, self.inf, self.inf, self.inf],
                [0, self.inf, self.inf, self.inf, self.inf, self.inf],
                [self.inf, self.inf, self.inf, -1, self.inf, self.inf],
                [self.inf, -1, self.inf, -1, self.inf, self.inf],
            ]
        ]
        expected = [
            [0, 1, 2, -1, 2, 1],
            [-1, 2, 3, -1, -1, 0],
            [-1, 2, 3, 3, 2, 1],
            [0, 1, 2, 3, 3, 2],
            [1, 2, 3, -1, 4, 3],
            [2, -1, 4, -1, 5, 4],
        ]
        self.run_funcs(args, expected)
