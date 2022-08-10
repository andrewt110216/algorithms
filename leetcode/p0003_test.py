from p0003_solution import Solution


class TestClass:

    # run test case for each implementation in Solution
    s = Solution()

    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = ["abcabcbb"]
        expected = 3
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = ["bbbbb"]
        expected = 1
        self.run_funcs(args, expected)

    def test3_example3(self):
        args = ["pwwkew"]
        expected = 3
        self.run_funcs(args, expected)

    def test4_empty(self):
        args = [""]
        expected = 0
        self.run_funcs(args, expected)

    def test5_repeats_at_start(self):
        args = ["aabcdef"]
        expected = 6
        self.run_funcs(args, expected)

    def test6_repeats_at_end(self):
        args = ["abcdeff"]
        expected = 6
        self.run_funcs(args, expected)

    def test7_multiple_repeats(self):
        args = ["aabcdaebefga"]
        expected = 5
        self.run_funcs(args, expected)
