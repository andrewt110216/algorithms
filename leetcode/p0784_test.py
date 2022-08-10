from p0784_solution import Solution
import copy


class TestClass:

    s = Solution()

    def run_funcs(self, args, expected):
        """Run test case for each implementation in Solution"""
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)

            # use a deep copy of args so side effects on pass-by-reference
            # variables do not persist for subsequent implementations
            args_copy = copy.deepcopy(args)
            result = func(*args_copy)

            # order of permutations does not matter
            # sort result and expected result for comparison
            for var in [result, expected]:
                var.sort()

            assert result == expected

    def test1_example1(self):
        args = ["a1b2"]
        expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = ["3z4"]
        expected = ["3z4", "3Z4"]
        self.run_funcs(args, expected)

    def test3_short_string_all_letters(self):
        args = ["abc"]
        expected = ["abc", "abC", "aBc", "aBC", "Abc", "AbC", "ABc", "ABC"]
        self.run_funcs(args, expected)

    def test4_long_string(self):
        args = ["aEi35bd6A"]
        expected = [
            "aei35bd6a",
            "aei35bd6A",
            "aei35bD6a",
            "aei35bD6A",
            "aei35Bd6a",
            "aei35Bd6A",
            "aei35BD6a",
            "aei35BD6A",
            "aeI35bd6a",
            "aeI35bd6A",
            "aeI35bD6a",
            "aeI35bD6A",
            "aeI35Bd6a",
            "aeI35Bd6A",
            "aeI35BD6a",
            "aeI35BD6A",
            "aEi35bd6a",
            "aEi35bd6A",
            "aEi35bD6a",
            "aEi35bD6A",
            "aEi35Bd6a",
            "aEi35Bd6A",
            "aEi35BD6a",
            "aEi35BD6A",
            "aEI35bd6a",
            "aEI35bd6A",
            "aEI35bD6a",
            "aEI35bD6A",
            "aEI35Bd6a",
            "aEI35Bd6A",
            "aEI35BD6a",
            "aEI35BD6A",
            "Aei35bd6a",
            "Aei35bd6A",
            "Aei35bD6a",
            "Aei35bD6A",
            "Aei35Bd6a",
            "Aei35Bd6A",
            "Aei35BD6a",
            "Aei35BD6A",
            "AeI35bd6a",
            "AeI35bd6A",
            "AeI35bD6a",
            "AeI35bD6A",
            "AeI35Bd6a",
            "AeI35Bd6A",
            "AeI35BD6a",
            "AeI35BD6A",
            "AEi35bd6a",
            "AEi35bd6A",
            "AEi35bD6a",
            "AEi35bD6A",
            "AEi35Bd6a",
            "AEi35Bd6A",
            "AEi35BD6a",
            "AEi35BD6A",
            "AEI35bd6a",
            "AEI35bd6A",
            "AEI35bD6a",
            "AEI35bD6A",
            "AEI35Bd6a",
            "AEI35Bd6A",
            "AEI35BD6a",
            "AEI35BD6A",
        ]
        self.run_funcs(args, expected)
