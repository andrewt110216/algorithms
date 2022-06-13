# Learning Algorithms
# Convert an Integer to String
# Andrew Tracey
# 6/13/2022

# DESCRIPTION
# Goal: Convert an integer to its string representation in decimal
# Method:
# While we may take this algorithm for granted, it may not be as simple 
# as it seems. We will prepare a string of the base digits, i.e.
# digits = '0123456789'. Then, it is easy to obtain the string represen-
# tation of an integer between 0 and 9, as digits[9] = "9".
# For larger integers, we need to find a way to reduce the problem down
# to single digit integers. This is an obvious candidate for recursion,
# and in each call, we will use floor and modulo division.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def algorithm(x):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    out = []

    def recurse(x):
        if x < 10:
            out.append(digits[x])
        else:
            remainder = x % 10
            x = x // 10
            recurse(x)
            recurse(remainder)

    recurse(x)

    return ''.join(out)

# ================================ TEST CASES ================================

if __name__ == '__main__':
    from datetime import datetime

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# Decorator Function for Testing Output --------------------------------------

    def test_decorator(func):
        """Decorator function to wrap around the algorithm"""
        def wrapper(expected, description, *args, **kwargs):
            global tests, failed_tests, divider_width
            tests += 1
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            print('Input:', *args, **kwargs)
            start = datetime.now()
            result = func(*args, **kwargs)
            print('Output:', result)
            print('Time:', datetime.now() - start)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Output: {expected_result}\n")
                failed_tests += 1

        return wrapper

    # For testing, decorate the algorithm function
    algorithm = test_decorator(algorithm)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Base'
    args = [12]
    kwargs = {}
    expected_result = '12'
    algorithm(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Base'
    args = [769]
    kwargs = {}
    expected_result = '769'
    algorithm(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Base'
    args = [6540980]
    kwargs = {}
    expected_result = '6540980'
    algorithm(expected_result, test_case_description, *args, **kwargs)

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
