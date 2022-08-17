from p0704_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)
            assert result == expected

    def test1_example1(self):
        args = [[-1, 0, 3, 5, 9, 12], 9]
        expected = 4
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[-1, 0, 3, 5, 9, 12], 2]
        expected = -1
        self.run_funcs(args, expected)

    def test3_length_1_match(self):
        args = [[1], 1]
        expected = 0
        self.run_funcs(args, expected)

    def test4_length_1_no_match(self):
        args = [[1], 2]
        expected = -1
        self.run_funcs(args, expected)

    def test5_target_at_end_even(self):
        args = [[1, 2, 3, 4, 5, 6], 6]
        expected = 5
        self.run_funcs(args, expected)

    def test6_target_at_end_odd(self):
        args = [[1, 2, 3, 4, 5, 6, 7], 7]
        expected = 6
        self.run_funcs(args, expected)

    def test7_target_at_start_even(self):
        args = [[1, 2, 3, 4, 5, 6], 1]
        expected = 0
        self.run_funcs(args, expected)

    def test8_target_at_start_odd(self):
        args = [[1, 2, 3, 4, 5, 6, 7], 1]
        expected = 0
        self.run_funcs(args, expected)
