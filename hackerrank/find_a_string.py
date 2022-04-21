# Hackerrank Problem
# Find a string
# Author: Andrew Tracey
# Completed: September 12, 2021

# --- PROBLEM DESCRIPTION ---
# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the
# given string. String traversal will take # place from left to right,
# not from right to left.

def count_substring(s, sub_s):
    matches = 0
    # loop through each character in string
    for string_char in range(0, len(s)):
        # if it matches the first character in sub_string, then loop through
        # each character in sub_string and compare to corresponding characters
        # in string. If you get to the end with a match, it's a match!
        if s[string_char] == sub_s[0]:
            for substring_char in range(1, len(sub_s)):
                if string_char + substring_char > len(s) - 1:
                    break
                if (sub_s[substring_char] ==
                        s[string_char + substring_char]):
                    if substring_char == len(sub_s) - 1:
                        matches += 1
                else:
                    break
    return matches


# --- INPUT OPTION --- Uncomment to take user input.
# string = input().strip()
# sub_string = input().strip()

# --- TEST CASES ---
print('--- TEST CASE 1 --- Expected Answer: 2 ---')
string = "ABCDCDC"
sub_string = "CDC"
result = count_substring(string, sub_string)
print(result)
assert result == 2

print('--- TEST CASE 2 --- Expected Answer: 1 ---')
string = "ABCDEFG"
sub_string = "DEF"
result = count_substring(string, sub_string)
print(result)
assert result == 1

print('--- TEST CASE 3 --- Expected Answer: 3 ---')
string = "ABCDEFGCDABcdEFGABCDC"
sub_string = "CD"
result = count_substring(string, sub_string)
print(result)
assert result == 3
