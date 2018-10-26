'''task_3.py

This testscript is intended to check copying file from VM to Host and in reverse order.

Arguments:
    This script requires three arguments (vm_username, host_username, file_name) to be passed in from the job_file,
    but these arguments need write before runing script and you have to rewrite the value of the rows in the my_testbed.yaml:
    (username: write_username,
     linux: write_password,
     ip: write IP,
     address: write IP,
     username: write_username,
     password: write_password) with the data given in the task.
    testbed: my_testbed.yaml
    
    vm_username: username of VM for connecting
    host_username: username of Host
    file_name: file name for creating and copying from VM to Host

You have to run script under easypy:
    $ easypy job_ez.py -testbed_file my_testbed.yaml --vm_username 'vm_name' --host_username 'hostname' --file_name 'file_name'
'''

__author__ = 'Yurii Kobuk'

from ats import aetest
from ats.topology import loader
from ats.aetest import test, setup, cleanup

from pyats.utils.fileutils import FileUtils

from sh import touch, rm


class MyTestcase(aetest.Testcase):
    '''Test case that connects to VM, creates, copies and deletes file for copying from VM to Host and in reverse order'''

    @setup
    def check_connect(self, testbed, vm_username, host_username, file_name):
        self.path_to_vm = 'sftp://localhost/home/{0}/{1}'.format(vm_username, file_name)
        self.path_to_host = '/home/{0}/{1}'.format(host_username, file_name)

        # Connect to VM by SSH and check
        self.vm = testbed.devices['vm']
        self.vm.connect()
        self.vm.execute('ping -c 4 google.com')
        self.vm.execute('ifconfig')

        # File for copy from VM to Host
        self.vm.execute('touch /home/{}/{}.txt'.format(vm_username, file_name))

        # Check new file
        self.vm.execute('ls -la /home/{}/ | grep {}'.format(vm_username, file_name))

        # SFTP connection
        self.futils = FileUtils(testbed=testbed)
        self.passed('New file for copy from VM to Host is created')

    @test
    def copy_from_vm_to_local(self, file_name):
        # Copying file from VM to Host
        self.futils.copyfile(source='{}.txt'.format(self.path_to_vm),
                             destination='{}.txt'.format(self.path_to_host))
        self.passed('The {} file has copied successfully '.format(file_name))

    @test
    def copy_from_local_to_vm(self, file_name):
        # Creates file for copy from host to VM
        touch("{}_copy.txt".format(self.path_to_host))

        # Copying file from Host to VM
        self.futils.copyfile(source='{}_copy.txt'.format(self.path_to_host),
                             destination='{}_copy.txt'.format(self.path_to_vm))

        self.passed('The {}_copy file has copied successfully '.format(file_name))

    @cleanup
    def clean_and_disconnect(self, vm_username, file_name):
        # Delete files from VM and Host, and disconnect
        self.futils.deletefile('{}.txt'.format(self.path_to_vm))
        self.futils.deletefile('{}_copy.txt'.format(self.path_to_vm))
        self.vm.execute('ls -la /home/{}/ | grep {}'.format(vm_username, file_name))
        rm('{}.txt'.format(self.path_to_host))
        rm('{}_copy.txt'.format(self.path_to_host))
        self.vm.destroy()
        self.passed('files {0}, {0}_copy were deleted'.format(file_name))


if __name__ == '__main__':
    aetest.main()
