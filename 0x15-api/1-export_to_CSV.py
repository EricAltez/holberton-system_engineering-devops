#!/usr/bin/python3
"""
export data in the CSV format.
"""
import csv
from sys import argv
import requests


if __name__ == '__main__':
    id = argv[1]
    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tod_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    r_todo = requests.get(tod_url).json()
    r_user = requests.get(us_url).json()

    with open('{}.csv'.format(id), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in r_todo:
            y = [id, r_user.get('username'),
                 x.get('completed'),
                 x.get('title')]
            y = [str(value) for value in y]
            csvwriter.writerow(y)
