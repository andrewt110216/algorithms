from p1029_solution import Solution
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
        args = [[[10, 20], [30, 200], [400, 50], [30, 20]]]
        expected = 110
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [
            [
                [259, 770],
                [448, 54],
                [926, 667],
                [184, 139],
                [840, 118],
                [577, 469],
            ]
        ]
        expected = 1859
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [
            [
                [515, 563],
                [451, 713],
                [537, 709],
                [343, 819],
                [855, 779],
                [457, 60],
                [650, 359],
                [631, 42],
            ]
        ]
        expected = 3086
        self.run_funcs(args, expected)
