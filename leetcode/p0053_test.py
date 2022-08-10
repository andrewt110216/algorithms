from p053_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
        expected = 6
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[1]]
        expected = 1
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[5, 4, -1, 7, 8]]
        expected = 23
        self.run_funcs(args, expected)

    def test4_empty_input(self):
        args = [[]]
        expected = 0
        self.run_funcs(args, expected)

    def test5_large_input(self):
        args = [list(range(100_000))]
        expected = sum(range(100_000))
        self.run_funcs(args, expected)
