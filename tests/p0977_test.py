from leetcode.p0977_solution import Solution
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
        args = [[1, 3, 7, 10, 12, 15]]
        expected = [1, 9, 49, 100, 144, 225]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[-7, -3, 2, 3, 11]]
        expected = [4, 9, 9, 49, 121]
        self.run_funcs(args, expected)

    def test3_single_element_positive(self):
        args = [[3]]
        expected = [9]
        self.run_funcs(args, expected)

    def test4_single_element_negative(self):
        args = [[-3]]
        expected = [9]
        self.run_funcs(args, expected)

    def test5_two_elements(self):
        args = [[-1, 5]]
        expected = [1, 25]
        self.run_funcs(args, expected)
