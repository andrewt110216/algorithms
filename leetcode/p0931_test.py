from p0931_solution import Solution
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
        args = [[[2, 1, 3], [6, 5, 4], [7, 8, 9]]]
        expected = 13
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[-19, 57], [-40, -5]]]
        expected = -59
        self.run_funcs(args, expected)

    def test3_example1_v2(self):
        args = [[[2, 1, 3], [6, 5, 4], [7, 8, 7]]]
        expected = 12
        self.run_funcs(args, expected)

    def test4_large_input(self):
        args = [
            [
                [80, 76, 17, 83, 71, 63, 19, 68, 23, 34, 97, 98],
                [52, 41, 88, 49, 54, 95, 23, 26, 11, 39, 93, 45],
                [41, 46, 21, 22, 30, 73, 84, 68, 47, 65, 88, 74],
                [42, 71, 70, 44, 99, 41, 50, 69, 61, 27, 91, 49],
                [59, 47, 56, 49, 67, 75, 38, 25, 11, 66, 64, 61],
                [75, 68, 64, 33, 59, 68, 86, 47, 33, 54, 57, 31],
                [68, 90, 40, 53, 69, 38, 83, 42, 92, 77, 42, 28],
                [15, 35, 81, 71, 54, 68, 92, 34, 19, 62, 90, 72],
                [97, 23, 73, 29, 85, 68, 58, 17, 94, 57, 49, 23],
                [68, 49, 45, 86, 23, 21, 58, 31, 92, 34, 34, 71],
                [50, 21, 62, 36, 72, 73, 71, 51, 54, 36, 57, 90],
                [17, 86, 84, 39, 59, 68, 11, 34, 19, 62, 21, 11],
            ]
        ]
        expected = 323
        self.run_funcs(args, expected)
