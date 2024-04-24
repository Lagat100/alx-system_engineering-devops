#!/usr/bin/python3
"""Using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_response = requests.get("https://jsonplaceholder\
            .typicode.com/users/{}".format(employee_id))
    todo_response = requests.get("https://jsonplaceholder\
            .typicode.com/todos?userId={}".format(employee_id))

    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    if todo_response.status_code != 200:
        print("Tasks not found")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('name')
    tasks_total = len(todo_data)
    tasks_done = sum(1 for task in todo_data if task.get('completed'))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, tasks_done, tasks_total))
    for task in todo_data:
        if task.get('completed'):
            print("\t{}".format(task.get('title')))
