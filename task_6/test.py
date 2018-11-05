import os
from ats import aetest

from ats.aetest import test, setup


class Smoke(aetest.Testcase):
    
    @setup
    def create(self, directory, report_directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        if not os.path.exists(report_directory):
            os.makedirs(report_directory)

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
