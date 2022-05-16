#!/usr/bin/python3
"""
returns information about employee TODO list progress.
"""


import requests
from sys import argv


if __name__ == "__main__":
    """ get user data and prints it """
    id = argv[1]
    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tod_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    r_todo = requests.get(tod_url).json()
    r_user = requests.get(us_url).json()

    task_total = 0
    task_completed = 0
    comp_task_list = []

    for task in r_todo:
        task_total += 1
        if task.get('completed') is True:
            task_completed += 1
            comp_task_list.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(r_user.get('name'), task_completed, task_total))
    for i in comp_task_list:
        print("\t {}".format(i))
