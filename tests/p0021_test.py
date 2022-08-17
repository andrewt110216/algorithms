from leetcode.p0021_solution import Solution
from data_structures.class_linked_list import list_to_ll


class TestClass:

    # run test case for each implementation in Solution
    s = Solution()

    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = list(map(list_to_ll, [[1, 2, 4], [1, 3, 4]]))
        expected = list_to_ll([1, 1, 2, 3, 4, 4])
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = list(map(list_to_ll, [[], []]))
        expected = list_to_ll([])
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = list(map(list_to_ll, [[], [0]]))
        expected = list_to_ll([0])
        self.run_funcs(args, expected)

    def test4_add_dups_and_negatives(self):
        args = list(map(list_to_ll, [[-2, 0, 1, 4, 4], [-8, -2, -1, 0, 3]]))
        expected = list_to_ll([-8, -2, -2, -1, 0, 0, 1, 3, 4, 4])
        self.run_funcs(args, expected)
