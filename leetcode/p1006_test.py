from p1006_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)
            assert result == expected

    def test1_example1(self):
        args = [4]
        expected = 7
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [10]
        expected = 12
        self.run_funcs(args, expected)

    def test3_odd_number(self):
        args = [5]
        expected = 7
        self.run_funcs(args, expected)

    def test4_larger_number(self):
        args = [21]
        expected = 23
        self.run_funcs(args, expected)

    def test5_larger_number_2(self):
        args = [99]
        expected = 98
        self.run_funcs(args, expected)

    def test5_largest_number(self):
        args = [1_000]
        expected = 1_001
        self.run_funcs(args, expected)
