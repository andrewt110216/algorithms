# Learning Algorithms
# [ALGORITHM]

# DESCRIPTION
# Goal:
# Method:
# 
# 
# 
# 
# 

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

def algorithm(i):
    """DOC STRING"""
    return i

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
                print(f"\t > Expected Output: {expected}\n")
                failed_tests += 1

        return wrapper

    # For testing, decorate the algorithm function
    algorithm = test_decorator(algorithm)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Base'
    args = [True]
    kwargs = {}
    expected_result = True
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
