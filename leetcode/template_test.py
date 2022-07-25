# **UPDATE 'template' FILENAME FOR IMPORT AND REMOVE THIS COMMENT**
from template_solution import Solution
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

            # TODO - OPTIONAL - DELETE THIS IF THE ORDER MATTERS ************
            # if result is list, sort it and expected result for comparison
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()
                    if type(var[0]) is list:
                        [x.sort() for x in var]

            assert result == expected

    def test1_example1(self):
        args = [True]
        expected = False
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [False]
        expected = True
        self.run_funcs(args, expected)
