from datetime import datetime
import copy


class PrintTests():
    """Use to print detail and summary of test case results"""

    def __init__(self, solution, cases):
        self.cases = cases
        self.solution = solution

        # make sure solution has an attribute called 'implementations'
        try:
            getattr(self.solution, "implementations")
        except AttributeError:
            raise AttributeError(
                "Solution must have an attribute 'implementations', which is"
                "a list of the names of the solution methods in Solution."
                )

        self.tests = 0
        self.failed_tests = 0
        self.print_width = 78
        self.max_io_len = 50

    def truncate_display(self, var):
        """Truncate the display of a long variable for printing to console"""
        if len(str(var)) > self.max_io_len:
            display = str(var)[:self.max_io_len // 2] + '... ' \
                        + str(var)[-self.max_io_len // 2:]
            return display
        else:
            return var

    def tuples_to_lists(self, var):
        """Check the input for any tuples, and convert them to lists"""

        # if var is not subscriptable, it has no tuples, so return it as is
        if not var or hasattr(var, "__getitem__") is False:
            return var

        # var must be a tuple, list, or dictionary
        # handle each type, looking for one layer of nested tuples, as well
        if type(var) is tuple:
            if type(var[0]) is not tuple:
                return list(var)
            else:
                return [list(x) for x in var]
        elif type(var) is list:
            if type(var[0]) is not tuple:
                return var
            else:
                return [list(x) for x in var]
        elif type(var) is dict:
            for key, value in var.items():
                if type(value) is tuple:
                    var[key] = list(value)
            return var

    def decorator(self, func):

        def wrapper(self, expected, *args):

            self.tests += 1
            start = datetime.now()
            result = func(*args)
            end = datetime.now()

            # check input/out for any tuples and convert them to lists
            result = self.tuples_to_lists(result)
            expected = self.tuples_to_lists(expected)

            # TODO: I need to pass a variable to determine if sorting should
            # be completed. Otherwise, I am forcing equality cases where the
            # list order matters (like sorting!)
            # if input/output is list, sort both for comparison
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()
                    if var and type(var[0]) is list:
                        [x.sort() for x in var]

            # truncate display of output/expected for printing to console
            result_display = self.truncate_display(result)
            expected_display = self.truncate_display(expected)

            # print and evaluate results
            print("    Output:", result_display)
            print("    Time:", end - start)
            if result == expected:
                print("\n  > Result: **PASS!**\n")
            else:
                self.failed_tests += 1
                print("\n  > Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_display}\n")

        return wrapper

    def summarize(self):

        # print number of tests run and failed, and overall results (pass/fail)
        print(" SUMMARY OF RESULTS ".center(self.print_width, "="))
        print(f"\nTOTAL TESTS RUN: {self.tests}")
        print("\nOVERALL RESULT:\n")

        if self.failed_tests:
            final_result = "FAIL."
            print(f"\t{self.failed_tests} test(s) failed.\n")
        else:
            final_result = "PASS!"
            print("\tAll tests passed! Niceee.\n")

        print("\t===========")
        print(f"\t|| {final_result} ||")
        print("\t===========\n")
        print("".center(self.print_width, '*'), "\n")

    def run(self):

        print()
        print(" RUNNING TEST CASES ".center(self.print_width, '*'))
        print()

        # run all test cases
        for description, args, expected in self.cases:
            print(f" CASE: {description} ".center(self.print_width, "-"))

            # truncate display of input for printing to console
            args_display = [self.truncate_display(arg) for arg in args]
            print('\nInput:', args_display, '\n')

            # execute test case for each implementation
            for func_str in self.solution.implementations:
                print(" - Implementation:", func_str)
                func = self.decorator(getattr(self.solution, func_str))

                # use a deep copy of args so side effects on pass-by-reference
                # variables do not persist for subsequent implementations
                args_copy = copy.deepcopy(args)
                func(self, expected, *args_copy)

        self.summarize()
