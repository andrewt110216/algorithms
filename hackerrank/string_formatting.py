# Hackerrank Problem
# String Formatting
# Author: Andrew Tracey
# Completed: December 7, 2021

# --- PROBLEM DESCRIPTION ---
# Given an integer n, print the following formats of each i from 1 to n:
#   - Decimal, Octal, Hexadecimal, Binary
#
# For each i, print each format of the number in a single line.
# Each format should be space-padded to equal the width of the Binary format
# Further, each format should be printed, separated by a space

def print_formatted(number):
    """
    Take number and print in decimal, octal, hexadecimal, binary
    """
    results = []
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        # add padding to decimal
        decimal = ' ' * (width - len(str(i))) + str(i)
        # get octal, add padding
        octal = oct(i)[2:]
        octal = ' ' * (width - len(octal)) + octal
        # get hexadecimal, add padding
        hexa = hex(i)[2:].upper()
        hexa = ' ' * (width - len(hexa)) + hexa
        # get binary
        binary = bin(i)[2:]
        binary = ' ' * (width - len(binary)) + binary
        # combine number formats into string and add to results
        result = ' '.join([decimal, octal, hexa, binary])
        results.append(result)

    # print results
    for line in results:
        print(line)


# --- TEST CASES ---
print('--- Test Case 1 ---')
print_formatted(26)

print('--- User Input ---')
print_formatted(int(input('Please input an integer:')))
