from p0344_solution import Solution
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
        args = [["h", "e", "l", "l", "o"]]
        expected = ["o", "l", "l", "e", "h"]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [["H", "a", "n", "n", "a", "h"]]
        expected = ["h", "a", "n", "n", "a", "H"]
        self.run_funcs(args, expected)

    def test3_single_element(self):
        args = [["a"]]
        expected = ["a"]
        self.run_funcs(args, expected)

    def test4_two_elements(self):
        args = [["a", "b"]]
        expected = ["b", "a"]
        self.run_funcs(args, expected)
