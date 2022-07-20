# 020 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

from collections import deque


class Solution:

    # list the methods to be run against the test cases
    implementations = ['valid_parentheses', 'valid_parentheses_first']

    def valid_parentheses(self, s: str) -> bool:
        """
        A stack is the proper data structure to confirm that open brackets are
        closed correctly. Add open brackets to the stack and when a closed
        bracket is encountered, pop from the stack and check that these two
        brackets match

        This implementation is simplified to be easier to read and validates
        that each character is in "()[]{}"

        Time: O(n) (iterate over s once)
        Space: O(n) (max length of the stack, if no closing brackets)
        """

        # adjacency lists for valid and matching brackets
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        stack = deque()  # store open brackets yet to be closed

        # iterate over each character in s
        # we are searching for any invalid brackets. if none found, s is valid
        for char in s:

            # if an open bracket, add it to the stack
            if char in opening:
                stack.append(char)

            # if a closing bracket, validate it against top bracket from stack
            elif char in closing:

                # check that the index of the top element from stack in the
                # opening brackets list matches the index of char
                # in the closing brackets list 
                if stack:
                    open = stack.pop()
                    if closing.index(char) != opening.index(open):
                        return False

                # if stack is empty, this closing bracket is invald
                else:
                    return False

            # if char is not in opening or closing lists, it is invalid
            else:
                return False

        # if stack is not empty, an open bracket was not closed so s is invalid
        if stack:
            return False

        # nothing invalid was found, so s must be valid
        return True


    def valid_parentheses_first(self, s: str) -> bool:
        """
        A stack is the proper data structure to confirm that open brackets are
        closed correctly. Add open brackets to the stack and when a closed
        bracket is encountered, pop from the stack and check that these two
        brackets match

        Time: O(n) (iterate over s once)
        Space: O(n) (max length of the stack, if no closing brackets)
        """

        stack = deque()  # store open brackets yet to be closed

        # iterate over each character in s
        # we are searching for any invalid brackets. if none found, s is valid
        for bracket in s:

            # if bracket is an open bracket, add it to the stack
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)

            # by assumptions, if not an open bracket, it is a closed bracket
            else:

                # if stack is empty, there is not a valid open bracket
                if not stack:
                    return False

                # pop an open bracket from the stack and validate
                open = stack.pop()
                if bracket == ")" and open != "(":
                    return False
                if bracket == "]" and open != "[":
                    return False
                if bracket == "}" and open != "{":
                    return False

        # if stack is not empty, an open bracket was not closed so s is invalid
        if stack:
            return False

        # nothing invalid was found, so s must be valid
        return True


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', ["()"], True],
        ['Example 2', ["()[]{}"], True],
        ['Example 3', ["(]"], False],
        ['Single Bracket', ["]"], False],
        ['Nested Example - Valid', ["([{()}])"], True],
        ['Nested Example - Invalid', ["([{()}[])"], False],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
