from leetcode.p0070_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)
            assert result == expected

    def test1_example1(self):
        args = [2]
        expected = 2
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [3]
        expected = 3
        self.run_funcs(args, expected)

    def test3_smallest_input(self):
        args = [1]
        expected = 1
        self.run_funcs(args, expected)

    def test4_medium_input(self):
        args = [5]
        expected = 8
        self.run_funcs(args, expected)

    def test5_large_input(self):
        args = [30]
        expected = 1_346_269
        self.run_funcs(args, expected)

    # n > 30 is too slow for iterative & brute force solutions

    # def test6_larger_input(self):
    #     args = [40]
    #     expected = 165_580_141
    #     self.run_funcs(args, expected)

    # def test7_largest_input(self):
    #     args = [45]
    #     expected = 1_836_311_903
    #     self.run_funcs(args, expected)
