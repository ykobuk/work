from ats import easypy
from pyats.topology import loader

testbed = loader.load('testbed.yaml')
sour_dir = testbed.custom.directory
rep_dir = testbed.custom['report_directory']

def main():
    easypy.run(testscript='test.py', directory=sour_dir, report_directory=rep_dir)
