# 344 - Reverse String
# https://leetcode.com/problems/reverse-string/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["reverse_string"]

    def reverse_string(self, s: list[str]) -> list[str]:
        """
        Use two pointers, left and right, and swap opposing elements of s,
        moving both pointers inwards on each iteration

        Time: O(n) (n/2 swaps are performed)
        Space: O(1) (constant space)
        """

        # set up pointers at the beginning and end of s
        left = 0
        right = len(s) - 1

        # swap left and right, move inwards, and repeat until left/right cross
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ["Example 1", [["h", "e", "l", "l", "o"]], ["o", "l", "l", "e", "h"]],
        [
            "Example 2",
            [["H", "a", "n", "n", "a", "h"]],
            ["h", "a", "n", "n", "a", "H"],
        ],
        ["Single Element", [["a"]], ["a"]],
        ["Two Elements", [["a", "b"]], ["b", "a"]],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
