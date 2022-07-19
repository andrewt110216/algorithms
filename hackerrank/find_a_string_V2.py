# Hackerrank Problem
# Find a string

# Version 2:
# This is my second script to solve this problem, more efficiently than the
# original script. I will attempt to use string comprehension.

# --- PROBLEM DESCRIPTION ---
# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the
# given string. String traversal will take # place from left to right,
# not from right to left.

def count_substring(s, sub_s):
    matches = sum([1 for x in range(len(s) - len(sub_s) + 1) if
                   s[x:x + len(sub_s)] == sub_s])
    return matches


# --- INPUT OPTION --- Uncomment lines to take user input.
# string = input().strip()
# sub_string = input().strip()
# count_substring(string, sub_string)

# --- TEST CASES ---
print('--- TEST CASE 1 --- Expected Answer: 2 ---')
string = "ABCDCDC"
sub_string = "CDC"
result = count_substring(string, sub_string)
print(result)
assert result == 2

print('--- TEST CASE 2 --- Expected Answer: 3 ---')
string = "ABCDCDC" + "EFCDCGDC"
sub_string = "CDC"
result = count_substring(string, sub_string)
print(result)
assert result == 3

print('--- TEST CASE 3 --- Expected Answer: 3 ---')
string = "ABCDEFGCDABcdEFGABCDC"
sub_string = "CD"
result = count_substring(string, sub_string)
print(result)
assert result == 3
