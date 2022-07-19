# NUM - NAME
# LINK

class Solution:

    # list the methods to be run against the test cases
    implementations = ['solution']

    def solution(self, my_boolean: bool) -> bool:
        """
        Describe the implementation

        Time: O(n)
        Space: O(n)
        """

        return not my_boolean


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        ['Example 1', [False], True],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
