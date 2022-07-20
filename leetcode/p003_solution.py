# 003 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:

    # list the methods to be run against the test cases
    implementations = ['longest_substring', 'longest_substring_check_all']

    def longest_substring(self, s: str) -> int:
        """
        Use a sliding window with two pointers, optimized by saving the highest
        index where each character is found in a dictionary so that the left
        pointer can jump ahead when repeat characters are encountered

        Time: O(n) (one pass through s)
        Space: O(n) (max size of the dictionary)
        """

        max_len = 0
        seen = {}  # store the highest index of each character
        i = 0  # left pointer

        # right pointer iterates over each character in s
        for j in range(len(s)):

            char = s[j]
            # if a 'char' exists in s at index i or to the right, slide i
            if char in seen and seen[char] >= i:
                i = seen[char] + 1

            # update max_len and add char to seen
            max_len = max(max_len, j - i + 1)
            seen[char] = j

        return max_len

    def longest_substring_check_all(self, s: str) -> str:
        """
        Use a sliding window with two pointers and check each substring of
        non-repeating characters (storing seen characters in a set), and
        dynamically update the maximum length

        Time: O(n) (one pass through s)
        Space: O(n) (max size of the set)
        """

        n = len(s)

        # check for empty string
        if n == 0:
            return 0

        seen = set()  # store seen characters in a set to check for repeats
        cur_len = 1  # length of current substring
        max_len = 1  # maximum substring length

        i = 0  # left pointer, sliding from first to 2nd-from-last element
        while i < n - 1:
            seen.add(s[i])

            # right pointer, j, will slide from i + 1 to last element
            j = i + 1
            while j < n:
                char = s[j]

                # if char is not a repeat, increment cur_len, update max_len,
                # add to seen, and increment j
                if char not in seen:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                    seen.add(char)
                    j += 1

                # if char is a repeat, end the current window from i
                else:
                    break

            # restart sliding window with next character
            i += 1
            seen.clear()
            cur_len = 1

        return max_len


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', ["abcabcbb"], 3],
        ['Example 2', ["bbbbb"], 1],
        ['Example 3', ["pwwkew"], 3],
        ['Empty String', [""], 0],
        ['Repeats Only at Start', ["aabcdef"], 6],
        ['Repeats Only at End', ["abcdeff"], 6],
        ['Multiple Repeats', ["aabcdaebefga"], 5],  # 'bcdae', 'cdaeb', 'befga'
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
