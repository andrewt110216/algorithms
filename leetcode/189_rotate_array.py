# Leetcode Problem #189
# Rotate Array

# PROBLEM DESCRIPTION
# Given an array, rotate the array to the right by k steps, where
# k is a non-negative integer

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]

# Follow up:
# There are at least 3 different ways to solve this problem.
# Can you do it in-place, with O(1) extra memorary?

# Notes
# We can directly place each number of the array in its required
# position by offsetting it by k, wrapping around the end (e.g. % n).
# But doing so will destroy the original element in that place, so
# we must store it in a temporary variable.
# Then, we place that temp val in its correct position. We repeat this
# n times to swap each element into its correct position.

# However, in the case that k is a factor of n (n%k=0), we will not hit
# every element, because we would cycle over only the subset of elements
# at positions 0, k, 2k, ..., n-k, 0, k, ...
# In this case, we must stop once we return to our starting position (0)
# and then increment our start position by 1 (1). Then we repeat these
# steps until we return to start. With each pass through the array,
# we are making n / k swaps, and as we increment our starting position
# we will cover each index from 0 to k - 1, or k start positions. 
# Therefore, we will make a total of k * (n/k) = n swaps, proving that
# we swap each element only one time, and make exactly n swaps.

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

def solution(nums: list, k: int) -> None:
    """Optimal solution, using cyclical replacements"""

    # Reduce k to be less than n, since each rotation after n
    # is a repeat rotation
    n = len(nums)
    k = k % n
    
    # Do nothing if k = 0
    if k > 0:
        start = 0
        swaps = 0
        while swaps < n:
            if debug: print(f'Begin new loop with start={start}, swaps={swaps}')
            i, temp = start, nums[start]
            if debug: print(f' > Current index={i}, Temp value={temp}')
            while True:
                j = (i + k) % n
                if debug: print(f'   > Dropping {temp} at index {j}, and saving {nums[j]}')
                nums[j], temp = temp, nums[j]
                swaps += 1
                i = j
                if debug: print(f'   > Swaps = {swaps}')
                if debug: print(f'     > The array is now: {nums}')
                # If we return to start, increment start, and break the loop
                if i == start:
                    if debug: print(f'  > Current index {i} equals start {start}. Moving start right by 1')
                    start += 1
                    break   

def solution0(nums: list, k: int) -> None:
    """Same as solution without debug statements, for readability"""
    n = len(nums)
    k %= n
    if k == 0:
        return

    start = 0
    swaps = 0
    while swaps < n:
        i = start
        temp = nums[i]
        while True:
            j = (i + k) % n
            nums[j], temp = temp, nums[j]
            swaps += 1
            i = j
            if i == start:
                start += 1
                break

def solution1(nums: list, k: int) -> None:
    """
    Using a new array
    Time Complexity = O(n)
    Space Complexity = O(n) (new array)
    """

    # Reduce k to less than length of nums
    n = len(nums)
    k %= n
    result = [0] * n

    # Copy each element from nums into result
    for i in range(n):
        j = (i + k) % n
        result[j] = nums[i]

    # Now, copy result into nums since this function returns None
    for i in range(n):
        nums[i] = result[i]


def solution2(nums: list, k: int) -> None:
    """
    Brute force solution.
    Time Complexity = O(n * k)
    Space Complexity = O(1) (in-place)
    """

    # Reduce k to less than length of nums
    n = len(nums)
    k %= n

    # Shift each element to the right, repeating k times
    for _ in range(k):
        previous = nums[-1]
        for i in range(n):
            nums[i], previous = previous, nums[i]


# ================================ TEST CASES ================================

if __name__ == '__main__':

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = True
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base Case 0 ".center(divider_width, "-"))
    tests += 1
    input_array = [1,2,3,4,5,6,7]
    k = 3
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [5,6,7,1,2,3,4]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base Case 1 ".center(divider_width, "-"))
    tests += 1
    input_array = [-1,-100,3,99]
    k = 2
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [3,99,-1,-100]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Empty ".center(divider_width, "-"))
    tests += 1
    input_array = [1, 2, 3, 4]
    k = 0
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [1, 2, 3, 4]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Single Element ".center(divider_width, "-"))
    tests += 1
    input_array = [1]
    k = 3
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [1]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: K > Len(Nums) ".center(divider_width, "-"))
    tests += 1
    input_array = [1, 2, 3, 4, 5]
    k = 12
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [4, 5, 1, 2, 3]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: K > Len(Nums) ".center(divider_width, "-"))
    tests += 1
    input_array = [1, 2, 3, 4, 5, 6]
    k = 4
    print('Input:', input_array, 'k:', k)
    solution(input_array, k)
    print('Output:', input_array)

    expected_result = [3, 4, 5, 6, 1, 2]
    if input_array == expected_result:
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"\t > Expected Result: {expected_result}\n")
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
