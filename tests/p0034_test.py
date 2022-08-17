from leetcode.p0034_solution import Solution


class TestClass:

    # run test case for each implementation in Solution
    s = Solution()

    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = [[5, 7, 7, 8, 8, 10], 8]
        expected = [3, 4]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[5, 7, 7, 8, 8, 10], 6]
        expected = [-1, -1]
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = [[], 0]
        expected = [-1, -1]
        self.run_funcs(args, expected)

    def test4_many_targets_at_start(self):
        args = [[-5, -5, -5, -1, 0, 0, 6, 100], -5]
        expected = [0, 2]
        self.run_funcs(args, expected)

    def test5_many_targets_at_end(self):
        args = [[0, 6, 100, 112, 112, 112, 112], 112]
        expected = [3, 6]
        self.run_funcs(args, expected)

    def test6_only_target_len_2(self):
        args = [[2, 2], 2]
        expected = [0, 1]
        self.run_funcs(args, expected)

    def test7_only_target_len_5(self):
        args = [[5, 5, 5, 5, 5], 5]
        expected = [0, 4]
        self.run_funcs(args, expected)

    def test8_no_target_len_2(self):
        args = [[2, 2], 3]
        expected = [-1, -1]
        self.run_funcs(args, expected)

    def test9_input_size_1(self):
        args = [[1], 1]
        expected = [0, 0]
        self.run_funcs(args, expected)
