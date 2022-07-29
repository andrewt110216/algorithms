# p784 - Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/


class Solution:

    # list the methods to be run against the test cases
    implementations = [
        "get_permutations_iterative",
        "get_permutations_recursive",
        "get_permutations_backtrack"
        ]

    def get_permutations_iterative(self, s: str) -> list[str]:
        """
        Build each permutation iteratively

        Initiate a list of the currently built permutations, starting with "".
        In an outer loop, iterate over each character, c, in s, and for each
        each previously built permutation, build new permutatuions by appending
        each possible 'case' of c (e.g. 'a' -> ['a', 'A'], '1' -> ['1'])

        Time: O(n * 2^n )
        Space: O()
        """

        permutations = [""]

        # iterate over s, adding to every previously built permutation
        # if s[i] is a letter, create new permutations for upper and lower case
        for c in s:
            cases = [c.lower(), c.upper()] if c.isalpha() else [c]
            new = []
            for permutation in permutations:
                [new.append(permutation + case) for case in cases]
            permutations = new

        return permutations

    def get_permutations_recursive(self, s: str) -> list[str]:
        """
        Use recursion to build each possible permutation of upper and lowercase
        letters in s

        Time: O( 2^n )
         - there at most 2^n permutations, in the case that all characters of s
           are letters, and constant work is done for each permutation
        Space: O( 2^n ) (max length of permutations and call stack)
        """

        permutations = []
        n = len(s)

        def recurse(i, cur):

            # base case: this recursive call built a full permutation
            if i == n:
                permutations.append(cur)

            # if s[i] is letter, add it to s as upper and lower and recurse
            elif s[i].isalpha():
                recurse(i + 1, cur + s[i].lower())
                recurse(i + 1, cur + s[i].upper())

            # if s[i] is not a letter, add it to s and continue recursing
            else:
                recurse(i + 1, cur + s[i])

        recurse(0, "")
        return permutations

    def get_permutations_backtrack(self, s: str) -> list[str]:
        """
        Use backtracking

        Time: O( 2^n )
         - there at most 2^n permutations, in the case that all characters of s
           are letters, and constant work is done for each permutation
        Space: O( 2^n ) (max length of permutations and call stack)
        """

        def recurse(i):

            # base case: current represents a full permutation
            if i == n:
                permutations.append(''.join(current))

            # add s[i] to current (in lower and upper case form) and recurse
            # to build a complete permutation, then backtrack (remove s[i])
            else:
                chars = [s[i].lower()]
                if s[i].isalpha():
                    chars.append(s[i].upper())
                for char in chars:
                    current.append(char)
                    recurse(i + 1)
                    current.pop()

        permutations = []
        current = []
        n = len(s)
        recurse(0)
        return permutations


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", ["a1b2"], ["a1b2", "a1B2", "A1b2", "A1B2"]],
        ["Example 2", ["3z4"], ["3z4", "3Z4"]],
        [
            "Short String All Letters",
            ["abc"],
            ["abc", "abC", "aBc", "aBC", "Abc", "AbC", "ABc", "ABC"],
        ],
        [
            "Long String",
            ["aEi35bd6A"],
            [
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
            ],
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases, ordered_d1=False)
    pt.run()
