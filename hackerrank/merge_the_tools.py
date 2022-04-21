# Hackerrank Problem
# Merge The Tools
# Author: Andrew Tracey
# Completed: January 15, 2022

# --- PROBLEM DESCRIPTION ---
# Consider the following:
#  - A string, s, of length n.
#  - an integer, k, where k is a factor of n.
# We can split s into (n / k) substrings where each subtring, t, consists of
# a contiguous block of k characters in s. Then, use each t to create string
# u such that:
#  - the characters in u are a subsequence of the characters in t.
#  - any repeat occurrence of a character is removed from the string such
#     that each character in u occurs exactly once.
#     In other words, if the character at some index j in u occurs at a
#     previous index i < j in t, then do not include the character in u.
#
# Given s and k, print (n / k) lines where each line i denotes string u(i).

def merge_the_tools(string, k):
    if len(string) == 0:
        print('\tERROR: string must be at least 1 character')
        return []
    if len(string) % k != 0:
        print('\tERROR: k must be a factor of len(string)')
        return []
    t_list = [string[i * k:i * k + k] for i in range(int(len(string) / k))]
    u_list = []
    for t in t_list:
        u = ''
        for c in t:
            if c not in u:
                u += c
        u_list.append(u)
    return u_list


# --- TEST CASES ---
print('--- Test Case 1 ---')
# Sample input provided by HR
result = merge_the_tools('AABCAAADA', 3)
print(f"\tResult: {result}")
assert result == ["AB", "CA", "AD"]
print('\tTest Passed!')

print('--- Test Case 2 ---')
# All one letter
result = merge_the_tools('ZZZZZZZZZZ', 2)
print(f"\tResult: {result}")
assert result == ["Z", "Z", "Z", "Z", "Z"]
print('\tTest Passed!')

print('--- Test Case 3 ---')
# No duplicate letters
result = merge_the_tools('ABCDEFGHIJ', 5)
print(f"\tResult: {result}")
assert result == ["ABCDE", "FGHIJ"]
print('\tTest Passed!')

print('--- Test Case 4 ---')
# Empty string
result = merge_the_tools('', 0)
print(f"\tResult: {result}")
assert result == []
print('\tTest Passed!')
