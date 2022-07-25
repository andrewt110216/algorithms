from p542_solution import Solution
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
        args = [[[0, 0, 0],[0, 1, 0],[0, 0, 0]]]
        expected = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[0, 0, 0],[0, 1, 0],[1, 1, 1]]]
        expected = [[0, 0, 0],[0, 1, 0],[1, 2, 1]]
        self.run_funcs(args, expected)

    def test3_larger_input(self):
        args = [
        [
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1 ,1, 1],
            [1, 1, 1], [0, 0, 0]
        ]
        ]
        expected = [
            [19, 19, 19], [18 ,18, 18], [17, 17, 17], [16, 16, 16],
            [15, 15, 15], [14 ,14, 14], [13, 13, 13], [12, 12, 12],
            [11, 11, 11], [10, 10, 10], [9, 9, 9], [8, 8, 8], [7, 7, 7],
            [6, 6, 6], [5, 5, 5], [4, 4, 4], [3, 3, 3], [2, 2, 2], [1, 1, 1],
            [0, 0, 0]
        ]
        self.run_funcs(args, expected)
