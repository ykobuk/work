from ats import aetest

from ats.aetest import test


class SmokeTest(aetest.Testcase):

    @test
    def div_test(self, num1, num2):
        if num2 == 0:
            self.passed("Test is passed, but it hasn't got result, because num2 got zero")
        else:
            result = num1 / num2
            if result < 0:
                self.failed('Test is failed, the result of div test: {}'.format(result))
            else:
                self.passed('Test is passed, the tesult of div test: {}'.format(result))


if __name__ == '__main__':
    aetest.main()
