import time
import argparse
import sys
from datetime import datetime, timedelta

from ats.easypy import Task


parser = argparse.ArgumentParser(description='Task_2')
parser.add_argument('--num1', type=float, required=True)
parser.add_argument('--num2', type=float, required=True)
# It isn't required, but if you want to see TimeoutError, run this script with --time 60
parser.add_argument('--time', type=int, default=1)


def main(runtime):
    print('Calculation tests result!!!')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    task_1 = Task(testscript='add_test.py',
                  runtime=runtime,
                  taskid='Add test',
                  num1=args.num1,
                  num2=args.num2)

    task_2 = Task(testscript='div_test.py',
                  runtime=runtime,
                  taskid='Division test',
                  num1=args.num1,
                  num2=args.num2)

    task_3 = Task(testscript='multiplication_test.py',
                  runtime=runtime,
                  taskid='Multiplication test',
                  num1=args.num1,
                  num2=args.num2)

    task_4 = Task(testscript='subtraction_test.py',
                  runtime=runtime,
                  taskid='Subtraction test',
                  num1=args.num1,
                  num2=args.num2)

    counter = timedelta(minutes=1)
    all_tasks = [task_1, task_2, task_3, task_4]
    for task in all_tasks:
        task.start()

    while counter:
        if any(task.is_alive() for task in all_tasks):
            time.sleep(5)
            counter -= timedelta(seconds=args.time)
            print(counter)
        else:
            break
    else:
        for task in all_tasks:
            task.terminate()
            task.join()
        raise TimeoutError('Not all tasks finished in 1 minutes!')
