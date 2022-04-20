# Learning Algorithms
# Binary Search - Recursive Approach
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

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def binary_search(sequence, target, start=0, end=False):
    """
    Return the index at which a target value is found in sequence.

    :param sequence: a list of unique values sorted in ascending order
    :param target: the value to be searched for in sequence
    :return index: the index of sequence at which target is found
    """

    if not end:
        end = len(sequence) - 1

    if end >= start:
        i = (start + end) // 2

        if sequence[i] == target:
            return i
        elif target < sequence[i]:  # target to left of i
            return binary_search(sequence, target, start, i - 1)
        elif target > sequence[i]:  # target to right of i
            return binary_search(sequence, target, i + 1, end)

    # Target was not found
    return False


# ================================ TEST CASES ================================

if __name__ == '__main__':

    import random

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = True
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
    length = 50  # Approximate, before removing duplicates
    sequence = list(set([random.randint(-length, length) for _ in range(length)]))
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
