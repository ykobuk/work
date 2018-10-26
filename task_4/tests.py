from ats import aetest

from ats.aetest import loop, test, setup


mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


class Test(aetest.Testcase):

    @setup
    def setup(self, letter):
        if letter in mapping:
            loop.mark(self.check, uid=mapping[letter])
            self.passed('The letter: {}'.format(letter))
        else:
            self.errored('You had to write a or b or c, not {}'.format(letter))

    @test
    def check(self, section):
        print("number : {}".format(section.uid))


if __name__ == '__main__':
    aetest.main()
