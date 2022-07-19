# Leetcode Problem #3
# Longest Substring Without Repeating Characters

# CATEGORY
# Strings, Sliding Windows

# PROBLEM DESCRIPTION
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not
# a substring.

# Constraints
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# AT NOTES
# 

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(s):
    # Use sliding window, optimized solution
        
    n = len(s)
    if n == 0:
        return 0
    
    max_len = 0
    i = 0
    seen = {}
    
    for j in range(n):
        if s[j] in seen:
            i = max(i, seen[s[j]]+1)
        max_len = max(max_len, j - i + 1)
        seen[s[j]] = j
    
    return max_len

def solution1(s):
    # Use sliding window to find longest substring from each starting position
    
    # Check for empty string
    n = len(s)
    if n == 0:
        return 0
    
    # set up variables
    seen = set()
    cur_len = 1
    max_len = 1
    
    # i will start from 0 and slide right to n - 2
    i = 0
    while i < n - 1:
        
        # for each i, j will start at i + 1 and slide right to n - 1
        j = i + 1
        seen.add(s[i])

        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                cur_len += 1
                max_len = max(max_len, cur_len)
                j += 1
            else:
                break
        
        # j has either reached the end, or found a repeat char
        # prepare to slide i right
        seen.clear()
        cur_len = 1
        i += 1
    
    return max_len 


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements, if any
    debug = False

    tests = 0
    failed_tests = 0
    divider_width = 78

# Decorator Function for Testing Output --------------------------------------

    def test_decorator(func):
        """Decorator function to wrap around the solution"""
        def wrapper(expected, description, *args, **kwargs):
            global tests, failed_tests, divider_width
            tests += 1
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            print('Input:', *args, **kwargs)
            result = func(*args, **kwargs)
            print('Output:', result)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_result}\n")
                failed_tests += 1

        return wrapper

    solution = test_decorator(solution)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = ["abcabcbb"]
    kwargs = {}
    expected_result = 3
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = ["bbbbb"]
    kwargs = {}
    expected_result = 1
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = ["pwwkew"]
    kwargs = {}
    expected_result = 3
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Empty'
    args = [""]
    kwargs = {}
    expected_result = 0
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Dup to start, none to end'
    args = ["aabcdef"]
    kwargs = {}
    expected_result = 6
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'No dups until end'
    args = ["abcdeff"]
    kwargs = {}
    expected_result = 6
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Challenging'
    args = ["aabcdaebefga"]
    kwargs = {}
    expected_result = 5
    solution(expected_result, test_case_description, *args, **kwargs)

# SUMMARY ====================================================================

    print(f" ALL RESULTS ".center(divider_width, "="))
    print(f"\nTOTAL TESTS RUN: {tests}")
    print("\nOVERALL RESULT:\n")
    if failed_tests:
        print(f"\t{failed_tests} test(s) failed.\n")
        print("\t===========")
        print("\t|| FAIL. ||")
        print("\t===========")
    else:
        print(f"\tAll tests passed! Niceee.\n")
        print("\t===========")
        print("\t|| PASS! ||")
        print("\t===========")
    print("".center(divider_width, '='))
