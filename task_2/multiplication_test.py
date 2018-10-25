from ats import aetest

from ats.aetest import test


class SmokeTest(aetest.Testcase):

    @test
    def multiplication_test(self, num1, num2):
        result = num1 * num2
        if result < 0:
            self.failed('Test is failed, the result of multiplication test: {}'.format(result))
        else:
            self.passed('Test is passed, the result of multiplication test: {}'.format(result))


if __name__ == '__main__':
    aetest.main()
