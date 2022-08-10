from p215_solution import Solution
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
        args = [[3, 2, 1, 5, 6, 4], 2]
        expected = 5
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]
        expected = 4
        self.run_funcs(args, expected)

    def test3_length_1(self):
        args = [[5], 1]
        expected = 5
        self.run_funcs(args, expected)

    def test4_length_2(self):
        args = [[5, 4], 2]
        expected = 4
        self.run_funcs(args, expected)

    def test5_add_negatives_zeroes_duplicates(self):
        args = [[-7, 9, -5, 0, 3, 9, -5, -1, 10, 8, 6, -1], 9]
        expected = -1
        self.run_funcs(args, expected)
