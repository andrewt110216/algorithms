from leetcode.p0141_solution import Solution
from data_structures.class_linked_list import ListNode, list_to_ll


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)
            assert result == expected

    def test1_example1(self):
        head1 = list_to_ll([3, 2, 0, -4])
        head1.next.next.next.next = head1.next
        head1.has_cycle = True  # prevent infinite recursion in __repr__
        args = [head1]
        expected = True
        self.run_funcs(args, expected)

    def test2_example2(self):
        head2 = list_to_ll([1, 2])
        head2.next.next = head2
        head2.has_cycle = True  # prevent infinite recursion in __repr__
        args = [head2]
        expected = True
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [ListNode(1)]
        expected = False
        self.run_funcs(args, expected)

    def test4_empty_input(self):
        args = [None]
        expected = False
        self.run_funcs(args, expected)

    def test5_two_nodes_no_cycle(self):
        args = [list_to_ll([1, 2])]
        expected = False
        self.run_funcs(args, expected)

    def test6_longer_list_no_cycle(self):
        args = [list_to_ll([1, 2, 0, 4, 5, 8])]
        expected = False
        self.run_funcs(args, expected)
