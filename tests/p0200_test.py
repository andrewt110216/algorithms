from leetcode.p0200_solution import Solution
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

            # if result is list, sort it and expected result for comparison
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()
                    if type(var[0]) is list:
                        [x.sort() for x in var]

            assert result == expected

    def test1_example1(self):
        args = [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ]
        expected = 1
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        ]
        expected = 3
        self.run_funcs(args, expected)

    def test3_small_island(self):
        args = [[["1"]]]
        expected = 1
        self.run_funcs(args, expected)

    def test4_small_water(self):
        args = [[["0"]]]
        expected = 0
        self.run_funcs(args, expected)

    def test5_all_land(self):
        args = [
            [
                ["1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
            ]
        ]
        expected = 1
        self.run_funcs(args, expected)

    def test6_all_water(self):
        args = [
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ]
        expected = 0
        self.run_funcs(args, expected)
