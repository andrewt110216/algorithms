from p0001_solution import Solution


class TestClass:

    # run test case for each implementation in Solution
    s = Solution()

    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = [[2, 7, 11, 15], 9]
        expected = [0, 1]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[3, 2, 4], 6]
        expected = [1, 2]
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[3, 3], 6]
        expected = [0, 1]
        self.run_funcs(args, expected)

    def test4_large_input(self):
        args = [list(range(10_001)), 19_999]
        expected = [9_999, 10_000]
        self.run_funcs(args, expected)

    def test5_no_solution(self):
        args = [[1, 2, 3, 4, 5], 10]
        expected = False
        self.run_funcs(args, expected)
