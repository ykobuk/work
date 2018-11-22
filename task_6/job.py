from ats import easypy

from pyats.topology import loader

testbed = loader.load('testbed.yaml')
directory = testbed.custom.directory
report_directory = testbed.custom['report_directory']


def main():
    easypy.run(testscript='test.py', directory=directory, report_directory=report_directory)
