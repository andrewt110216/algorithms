# **UPDATE 'template' FILENAME FOR IMPORT AND REMOVE THIS COMMENT**
from template_solution import Solution


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = [True]
        expected = False
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [False]
        expected = True
        self.run_funcs(args, expected)
