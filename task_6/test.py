import os
from ats import aetest

from ats.aetest import test, setup
from pyats.topology.loader import load


class Smoke(aetest.Testcase):
    
    @setup
    def create(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @test
    def foo(self, directory):
        with open(f'{directory}/foo.txt', 'w') as file:
            file.write('Some important info: foo')

    @test
    def bar(self, directory):
        with open(f"{directory}/bar.txt", 'w') as file:
            file.write('Some important info: bar')


if __name__ == "__main__":
    aetest.main()
