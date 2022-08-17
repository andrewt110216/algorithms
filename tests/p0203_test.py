import copy
from leetcode.p0203_solution import Solution
from data_structures.linked_list import list_to_ll


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
        args = [list_to_ll([1, 2, 6, 3, 4, 5, 6]), 6]
        expected = list_to_ll([1, 2, 3, 4, 5])
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [list_to_ll([]), 1]
        expected = None
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [list_to_ll([7, 7, 7, 7]), 7]
        expected = None
        self.run_funcs(args, expected)

    def test4_every_other_node_is_val(self):
        args = [list_to_ll([5, 2, 5, 7, 5, 4, 5]), 5]
        expected = list_to_ll([2, 7, 4])
        self.run_funcs(args, expected)
