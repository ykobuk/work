"""Run this script in terminal:

   1) By default arguments: python test_calculation.py
   2) With arguments: python test_calculation.py -num1 any_number -num2 any_number
"""
import argparse
import sys
from calculation import add, divide

from ats import aetest
from ats.aetest import test


class SmokeTest(aetest.Testcase):
    """Testing divide and add functions from calculation.py"""

    @test
    def test_divine_function(self, num1, num2):
        try:
           result = divide(num1, num2)
           if result < 0:
               self.skipped("Result of divide function less than 0, got {}".format(result))
        except ZeroDivisionError:
            self.passx('Division by zero', from_exception=ZeroDivisionError("Sorry, I can't do it!"))
        else:
            self.passed('Passed, result of divide function: {}'.format(result))

    @test
    def test_add_function(self, num1, num2):
        result = add(num1, num2)
        if result < 0:
            self.skipped("Result of add function less than 0, got {}".format(result))
        else:
            self.passed("Passed, result of add function: {}".format(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='standalone parser')
    parser.add_argument('-num1', dest='num1', type=int, required=False, default=3)
    parser.add_argument('-num2', dest='num2', type=int, required=False, default=0)

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    print(args)
    aetest.main(num1=args.num1, num2=args.num2)


