#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
to export data in the JSON format.
Requirements:
    Records all tasks from all employees
    Format must be: /{ "USER_ID": [ {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
    "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    file = 'todo_all_employees.json'
    url1 = 'https://jsonplaceholder.typicode.com/users'
    users = get(url1).json()
    _json = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        tasks = get(url1 + '/' + str(user_id) + '/todos').json()
        my_list = []
        for task in tasks:
            _dict = {}
            _dict["username"] = username
            _dict["task"] = task["title"]
            _dict["completed"] = task["completed"]
            my_list.append(_dict)
        _json[user_id] = my_list
    with open(file, 'w') as f:
        json.dump(_json, f)
