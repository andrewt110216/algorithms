from p617_solution import Solution
from class_binary_tree import array_to_tree


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)

            assert result == expected

    def test1_example1(self):
        args = [array_to_tree([1, 3, 2, 5]), array_to_tree([2, 1, 3, None, 4, None, 7])]
        expected = array_to_tree([3, 4, 5, 5, 4, None, 7])
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [array_to_tree([1]), array_to_tree([1, 2])]
        expected = array_to_tree([2, 2])
        self.run_funcs(args, expected)

    def test3_empty_input(self):
        args = [array_to_tree([]), array_to_tree([])]
        expected = array_to_tree([])
        self.run_funcs(args, expected)

    def test4_all_overlap(self):
        args = [array_to_tree([10, 20, 30, 40, 50]), array_to_tree([1, 2, 3, 4, 5])]
        expected = array_to_tree([11, 22, 33, 44, 55])
        self.run_funcs(args, expected)

    def test5_no_overlap(self):
        args = [
            array_to_tree([0, 1, None, 3, 4]),
            array_to_tree([0, None, 2, None, None, 5, 6]),
        ]
        expected = array_to_tree([0, 1, 2, 3, 4, 5, 6])
        self.run_funcs(args, expected)
