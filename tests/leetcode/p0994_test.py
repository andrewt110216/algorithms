from leetcode.p0994_solution import Solution
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
        args = [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]
        expected = 4
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]]
        expected = -1
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[[0, 2]]]
        expected = 0
        self.run_funcs(args, expected)

    def test4_multiple_rotten_at_start(self):
        args = [
            [
                [2, 1, 1, 1],
                [1, 1, 0, 0],
                [0, 1, 0, 2],
                [1, 1, 0, 1],
                [0, 0, 1, 1],
            ]
        ]
        expected = 5
        self.run_funcs(args, expected)
