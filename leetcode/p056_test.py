from p056_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            result = func(*args)

            # if result is list, sort it and expected result for comparison
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()
                    if type(var[0]) is list:
                        [x.sort() for x in var]

            assert result == expected

    def test1_example1(self):
        args = [[[1, 3], [2, 6], [8, 10], [15, 18]]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[1, 4], [4, 5]]]
        expected = [[1, 5]]
        self.run_funcs(args, expected)

    def test3_one_interval(self):
        args = [[[1, 5]]]
        expected = [[1, 5]]
        self.run_funcs(args, expected)

    def test4_no_overlap(self):
        args = [[[1, 3], [5, 7], [8, 10]]]
        expected = [[1, 3], [5, 7], [8, 10]]
        self.run_funcs(args, expected)

    def test5_all_overlap(self):
        args = [[[1, 3], [2, 4], [3, 5]]]
        expected = [[1, 5]]
        self.run_funcs(args, expected)

    def test6_decrease_start_interval(self):
        args = [[[1, 4], [0, 4]]]
        expected = [[0, 4]]
        self.run_funcs(args, expected)

    def test6_two_overlaps(self):
        args = [[[1, 3], [2, 6], [8, 10], [15, 18]]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.run_funcs(args, expected)

    def test7_no_overlap_not_sorted(self):
        args = [[[1, 4], [0, 0]]]
        expected = [[0, 0], [1, 4]]
        self.run_funcs(args, expected)
