# Python 3.6.7

Create virtualenv
```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
$ sudo apt-get install python3.6-dev
$ sudo apt-get install virtualenv
$ mkdir new_folder
$ cd new_folder/
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ git clone https://github.com/asstelite/work.git
```

# task_1
1. In virtualenv:
```
  - Run by default arguments: $ python test_calculation.py
  - Run with arguments: $ python test_calculation.py -num1 any_number -num2 any_number
```

# task_2
1. In virtualenv:
```
  - Run with arguments:$ easypy job_file.py --num1 any_number --num2 any_number
```

# task_3
1. In terminal
```
- $ pip install sh
- $ pip install paramiko
```

2.  my_testbed.yaml
```
- Write username, password, IP from task
```

3. Run job_ez.py with arguments in virtualenv:

```
arguments:
--vm_username - username of VM for connecting
--host_username - username of Host
--file_name - file name for creating and copying from VM to Host

$ easypy job_ez.py -testbed_file my_testbed.yaml --vm_username 'vm_name' --host_username 'hostname' --file_name 'file_name'
```

# task_4
1. In virtualenv:
```
  - Run with argument:$ easypy job_tests.py --letter 'write "a" or "b" or "c"'
```

# task_5
1. In terminal:
```
- sudo docker pull asstelite/my-tests
- sudo docker run -it -v $(pwd)/archive:/my-tests/archive asstelite/my-tests easypy job_rabbit.py --word "any word"
The archive of report will be in folder $(pwd)/archive
```

# task_6
1. In terminal:
```
- easypy -configuration plugins/plugins.yaml job.py archive_dir data

```
