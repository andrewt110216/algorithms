# Learning Algorithms
# Binary Search - Iterative Approach
# Andrew Tracey
# April 19, 2022

# DESCRIPTION
# Goal: Return the index of a target value in a sorted sequence (e.g. a list)
# Method: Basically, play Irish poker. Start by guessing the middle element.
# If this is greater than the target, then move the "end" of the relevant range
# to the element to the left of the middle. If it is less than the target, then
# move the "start" of the relevant range to the element to the right of the
# middle. Then, guess the middle of the new relevant range. Repeat this process
# until the target is found, or return False if not found.

# Assume the sequence contains unique elements.

# Iterative approach. Perhaps more intuitive.
# Runtime is O(logn), because in the worst case, the array of size n is halved
# as many times as necessary until there is just 1 element remaining, which is
# the definition of log2(n).

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def binary_search(sequence, target):
    """
    Return the index at which a target value is found in sequence.

    :param sequence: a list of unique values sorted in ascending order
    :param target: the value to be searched for in sequence
    :return index: the index of sequence at which target is found
    """
    n = len(sequence)
    start = 0
    end = n - 1
    while start <= end:
        i = (start + end) // 2
        if debug: print(f"Checking midpoint {i} of [{start}:{end}]...")
        if target > sequence[i]:
            start = i + 1
            if debug: print(f"\t{target} > {sequence[i]}. Shifting right.")
        elif target < sequence[i]:
            end = i - 1
            if debug: print(f"\t{target} < {sequence[i]}. Shifting left.")
        else:  # sequence[index] == target
            if debug: print(f"\tIt was a match! Returning {i}")
            return i
    return False

# ================================ TEST CASES ================================

if __name__ == '__main__':

    import random

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_input = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    print('Input:', test_input)
    result = binary_search(*test_input)
    print('Output:', result)

    expected_result = 4
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result was {expected_result}\n")
        failed_btests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_input = ([], 1)
    print('Input:', test_input)
    result = binary_search(*test_input)
    print('Output:', result)

    expected_result = False
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result was {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    length = 1000
    sequence = list(set([random.randint(-1000, 1000) for _ in range(length)]))
    target = sequence[random.randint(1, len(sequence))-1]
    sequence.sort()
    test_input = (sequence, target)
    print('Input:', test_input)
    result = binary_search(*test_input)
    print('Output:', result)

    expected_result = sequence.index(target)
    if result == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result was {expected_result}\n")
        failed_tests += 1

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
