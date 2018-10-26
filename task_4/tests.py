'''tests.py

This test script is intended to looping of 'check' test as many times as many
numbers in the 'mapping' dictionary for the given letter.

Arguments:
    This script requires one argument (letter) to be passed in from the job_file (job_tests.py)
    letter: Have to write 'a' or 'b' or 'c' .

Run script under easypy:
    $ easypy job_tests.py --letter 'write "a" or "b" or "c"'

'''

__author__ = 'Yurii Kobuk'

from ats import aetest

from ats.aetest import loop, test, setup


mapping = {
    'a': (1, 3, 4, 5, 6, 7, 8),
    'b': (0, 2, 3, 4),
    'c': (7, 9, 0, 6, 5, 4, 3, 1),
}


class Test(aetest.Testcase):
    '''Testcase that takes one letter and ckecks if the letter is on mapping.
    If the letter in on mapping the check function will make looping as many times
    as many numbers in the 'mapping dictionary for the given number'
    '''
    
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
