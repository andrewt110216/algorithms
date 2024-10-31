# Knuth-Morris-Pratt - String Pattern Matching
# Uses prefix-suffix table to improve on brute force approach

# Analysis
#  Case     TC        SC    Comments
#  ----     --        --    --------
#  Worst    O(n * m)  O(m)  pattern is matched at each index of text
#  Average  O(n + m)  O(m)  number of matches is independent of n
#  Best     O(n)      O(m)  first char of pattern is not in text

# n := the length of text
# m := the length of pattern

from algorithms.boyer_moore import test_cases


def knuth_morris_pratt(text: str, pattern: str):
    """Returns a list of indices in text at which pattern occurs"""

    n = len(text)
    m = len(pattern)

    # handle edges cases where match is not possible
    if m == 0 or n == 0 or m > n:
        return []

    matches = []
    ps_tbl = _get_prefix_suffix_table(pattern)

    # i is current index of text to align with beginning of pattern
    # j is current index of pattern for comparison to index i + j of text
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            j += 1
            i += 1
            if j == m:
                matches.append(i - m)
                j = 0
        else:
            if j == 0:
                i += 1
            else:
                j = ps_tbl[j - 1]

    return matches


def _get_prefix_suffix_table(pattern):
    """
    Returns the prefix-suffix table for the KMP algorithm
    Provides the length of the longest proper prefic that is also a suffix in
    the substring of pattern ending with index i
    """

    tbl = [0] * len(pattern)
    i, j = 0, 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            tbl[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = tbl[i - 1]
            else:
                tbl[i] = 0
                j += 1
    return tbl


test_cases = [
    # text, pattern, expected results
    ("", "", []),  # empty strings
    ("aa", "", []),  # pattern is empty string
    ("", "a", []),  # text is empty string
    ("ab", "abc", []),  # pattern too long
    ("abc", "abc", [0]),  # exact match
    ("abcd", "abc", [0]),  # match at start
    ("aaaba", "aab", [1]),  # match in middle
    ("abcde", "cde", [2]),  # match at end
    ("aaaaa", "a", [0, 1, 2, 3, 4]),  # match at each index
    ("aaaaaaaa", "aaa", [0, 1, 2, 3, 4, 5]),  # longer match at each index
    ("aabaabaacaaxyzaabaac", "aabaac", [3, 14]),  # match using suffix
    ("01010101", "01", [0, 2, 4, 6]),  # text is pattern repeated
    ("abcdefg", "cbc", []),  # no match
]

if __name__ == "__main__":

    for text, pattern, expected in test_cases:
        matches = knuth_morris_pratt(text, pattern)
        print(".", end="") if matches == expected else print("x", end="")
    print()

    # Tests for prefix-suffix table subroutine
    # pattern, expected lps table
    patterns = [
        ("a", [0]),  # prefix cannot be length of string
        ("aa", [0, 1]),
        ()
    ]
