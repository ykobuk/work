import os
from ats import aetest

from ats.aetest import test, setup
from pyats.topology.loader import load


class Smoke(aetest.Testcase):
    
    @setup
    def create(self, testbed):
        self.directory = testbed.custom.directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    @test
    def foo(self):
        with open('{}/foo.txt'.format(self.directory), 'w') as file:
            file.write('Some important info: foo')

    @test
    def bar(self):
        with open("{}/bar.txt".format(self.directory), 'w') as file:
            file.write('Some important info: bar')


if __name__ == "__main__":
    aetest.main()
