# Boyer-Moore (Bad Character Heuristic) - String Pattern Matching
# Uses bad character table to improve on brute force approach

# Analysis
#  Case     TC        SC    Comments
#  ----     --        --    --------
#  Worst    O(n * m)  O(m)  pattern is matched at each index of text
#  Average  O(n + m)  O(m)  number of matches is independent of n
#  Best     O(n)      O(m)  first char of pattern is not in text

# n := the length of text
# m := the length of pattern


def boyer_moore(text: str, pattern: str):
    """Returns a list of indices in text at which pattern occurs"""

    n = len(text)
    m = len(pattern)

    # handle edge cases where match is not possible
    if m == 0 or n == 0 or m > n:
        return []

    bad_chars = _get_bad_character_table(pattern)
    matches = []

    # current index of text to align with beginning of pattern
    i = 0
    while i <= n - m:

        # compare pattern to current substring of text in reverse order using j
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # if pattern matches text at i, j will equal -1
        if j < 0:
            matches.append(i)

            # exit loop if i is in its last valid position
            if i + m >= n:
                break
            else:
                next_char = text[i + m]
                # if next_char exists in pattern, we can advance i to align
                # next_char with its last occurence in pattern
                # otherwise, we can advance i all the way past next_char by
                # using the fact that bad_char returns -1
                i += m - bad_chars[ord(next_char)]

        # if pattern does not match at i, determine how much to advance i
        else:
            cur_char = text[i + j]
            # if cur_char exists in pattern to the right of j we can only
            # increment i by 1 (we don't want to move i to the left)
            last_occurence = bad_chars[ord(cur_char)]
            if last_occurence > j:
                i += 1
            # otherwise we can advance i so that cur_char aligns with its last
            # occurence in pattern
            else:
                i += j - last_occurence

    return matches


def _get_bad_character_table(pattern):
    """
    Returns the bad character table for the Boyer-Moore algorithm using ASCII
    Provides the last index in pattern at which the ith alphabet char exists
    Uses -1 if ith char is not in pattern
    """

    tbl = [-1] * 256
    for i, char in enumerate(pattern):
        tbl[ord(char)] = i
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
        matches = boyer_moore(text, pattern)
        print(".", end="") if matches == expected else print("x", end="")
    print()
