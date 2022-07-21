from datetime import datetime


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
        self.max_io_print_len = 50

    def decorator(self, func):

        def wrapper(self, expected, *args):

            self.tests += 1
            start = datetime.now()
            result = func(*args)
            end = datetime.now()

            # if output is list, sort result and expected result for comparison
            for var in [result, expected]:
                if type(var) is list:
                    var.sort()
                    if type(var[0]) is list:
                        [x.sort() for x in var]

            # print and evaluate results
            print("    Output:", str(result)[:self.max_io_print_len])
            print("    Time:", end - start)
            if result == expected:
                print("\n  > Result: **PASS!**\n")
            else:
                self.failed_tests += 1
                print("\n  > Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected}\n")

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

            # truncate printing of very large input
            args_display = []
            for arg in args:
                if len(str(arg)) > self.max_io_print_len:
                    display = str(arg)[:self.max_io_print_len // 2]
                    display += '... ' + str(arg)[-self.max_io_print_len // 2:]
                else:
                    display = arg
                args_display.append(display)

            print('\nInput:', args_display, '\n')

            # execute test case for each implementation
            for func_str in self.solution.implementations:
                print(" - Implementation:", func_str)
                func = self.decorator(getattr(self.solution, func_str))
                func(self, expected, *args)

        self.summarize()
