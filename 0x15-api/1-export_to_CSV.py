#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the CSV format.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user = get(url1).json()
    user = user['username']
    tasks = get(url1 + '/todos').json()
    _file = argv[1] + ".csv"
    with open(_file, 'w') as f:
        _writer = csv.writer(f, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        for task in tasks:
            _writer.writerow([argv[1], user, task['completed'], task['title']])
