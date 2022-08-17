from p0120_solution import Solution
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

            assert result == expected

    def test1_example1(self):
        args = [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]]
        expected = 11
        self.run_funcs(args, expected)

    def test2_example2(self):
        args = [[[-10]]]
        expected = -10
        self.run_funcs(args, expected)

    def test3_slightly_larger(self):
        args = [[[1], [2, 3], [5, 4, 3], [6, 7, 5, 8], [10, 9, 11, 6, 7]]]
        expected = 18
        self.run_funcs(args, expected)

    def test4_add_negatives(self):
        args = [[[-2], [3, 4], [-6, -5, -7], [4, 1, 8, 3]]]
        expected = -4
        self.run_funcs(args, expected)

    def test5_large_input(self):
        args = [
            [
                [68],
                [434, 940],
                [588, 869, 500],
                [806, 433, 806, 55],
                [875, 458, 585, 123, 104],
                [825, 414, 574, 476, 108, 172],
                [553, 143, 311, 142, 753, 752, 729],
                [140, 855, 707, 422, 37, 101, 117, 524],
                [229, 839, 986, 207, 648, 175, 820, 240, 18],
                [472, 859, 838, 117, 196, 498, 393, 364, 529, 997],
                [98, 347, 457, 548, 807, 760, 609, 116, 607, 586, 874],
                [645, 840, 161, 183, 350, 746, 672, 322, 467, 642, 929, 790],
                [
                    642,
                    160,
                    350,
                    632,
                    134,
                    381,
                    44,
                    364,
                    266,
                    167,
                    151,
                    987,
                    855,
                ],
                [
                    10,
                    104,
                    168,
                    614,
                    769,
                    899,
                    15,
                    269,
                    379,
                    862,
                    924,
                    839,
                    106,
                    579,
                ],
                [
                    240,
                    966,
                    88,
                    866,
                    292,
                    224,
                    136,
                    883,
                    344,
                    29,
                    473,
                    418,
                    329,
                    124,
                    636,
                ],
                [
                    859,
                    89,
                    582,
                    291,
                    14,
                    586,
                    391,
                    157,
                    613,
                    316,
                    840,
                    914,
                    61,
                    942,
                    899,
                    100,
                ],
                [
                    946,
                    741,
                    10,
                    996,
                    708,
                    576,
                    407,
                    776,
                    826,
                    467,
                    476,
                    699,
                    21,
                    749,
                    952,
                    155,
                    105,
                ],
                [
                    330,
                    404,
                    576,
                    447,
                    151,
                    577,
                    765,
                    640,
                    636,
                    797,
                    647,
                    795,
                    209,
                    570,
                    362,
                    348,
                    108,
                    938,
                ],
                [
                    283,
                    826,
                    303,
                    42,
                    307,
                    482,
                    418,
                    95,
                    388,
                    844,
                    811,
                    620,
                    177,
                    919,
                    503,
                    435,
                    636,
                    406,
                    786,
                ],
            ]
        ]
        expected = 5469
        self.run_funcs(args, expected)
