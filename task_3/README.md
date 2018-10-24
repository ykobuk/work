steps to run task_3

1. Create virtualenv

```
$ mkdir new_folder
$ cd new_folder/
$ virtualenv -p python3.5 venv
$ source venv/bin/activate
$ sudo apt-get install python3.5-dev
$ pip install -r requirements.txt
```

2.  my_testbed.yaml

```
write username, password, IP from task
```

3. Run job_ez.py with arguments:

```
arguments:
--vm_username - username of VM for connecting
--host_username - username of Host
--file_name - file name for creating and copying from VM to Host

$ easypy job_ez.py -testbed_file my_testbed.yaml --vm_username 'vm_name' --host_username 'hostname' --file_name 'file_name'

