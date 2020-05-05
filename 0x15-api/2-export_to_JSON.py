#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to
export data in the JSON format.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: '{' "USER_ID": [ {"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
    File name must be: USER_ID.json
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    url1 = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    user = get(url1).json()
    user = user['username']
    tasks = get(url1 + '/todos').json()
    file = argv[1] + '.json'
    my_list = []
    _json = {}
    for task in tasks:
        _dict = {}
        _dict["task"] = task["title"]
        _dict["completed"] = task["completed"]
        _dict["username"] = user
        my_list.append(_dict)
    _json[argv[1]] = my_list
    with open(file, 'w') as f:
        json.dump(_json, f)
