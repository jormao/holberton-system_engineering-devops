#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user = get(url1).json()
    user = user['name']
    tasks = get(url1 + '/todos').json()
    full_task = 0
    count = 0
    for task in tasks:
        full_task += 1
        if task['completed']:
            count += 1
    print("Employee {} is done with tasks({}/{}):".format(user, count,
                                                          full_task))
    for task in tasks:
        if task['completed']:
            print('\t {}'.format(task['title']))
