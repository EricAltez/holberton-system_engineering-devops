#!/usr/bin/python3
"""Exports to a json file"""
import json
from sys import argv
import requests


if __name__ == '__main__':
    us_url = 'https://jsonplaceholder.typicode.com/users/'
    tod_url = 'https://jsonplaceholder.typicode.com/todos'

    r_todo = requests.get(tod_url).json()
    r_user = requests.get(us_url).json()

    with open('todo_all_employees.json', 'w') as js:
        info = {}
        for x in r_user:
            id = x.get('id')
            tsk = []
            for r in r_todo:
                if r.get('userId') == id:
                    tsk.append({'username': x.get('username'),
                                'task': r.get('title'),
                                'completed': r.get('completed')})
            info[str(id)] = tsk
        json.dump(info, js)
