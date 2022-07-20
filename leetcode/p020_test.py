from p020_solution import Solution


class TestClass:

    # run test case for each implementation in Solution
    s = Solution()

    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = ["()"]
        expected = True
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = ["()[]{}"]
        expected = True
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = ["(]"]
        expected = False
        self.run_funcs(args, expected)

    def test4_single_backet(self):
        args = ["]"]
        expected = False
        self.run_funcs(args, expected)

    def test5_nested_valid(self):
        args = ["([{()}])"]
        expected = True
        self.run_funcs(args, expected)

    def test6_nested_invalid(self):
        args = ["([{()}[])"]
        expected = False
        self.run_funcs(args, expected)
