from p0148_solution import Solution
from class_linked_list import list_to_ll


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)
            assert result == expected

    def test1_example1(self):
        args = [None]
        expected = None
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [list_to_ll([-1, 5, 3, 4, 0])]
        expected = list_to_ll([-1, 0, 3, 4, 5])
        self.run_funcs(args, expected)

    def test3_longer_list(self):
        args = [list_to_ll([10, -2, 9, 7, 5, 4, 0, -2, -5, 8])]
        expected = list_to_ll([-5, -2, -2, 0, 4, 5, 7, 8, 9, 10])
        self.run_funcs(args, expected)
