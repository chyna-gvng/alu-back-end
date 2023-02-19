#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""
import json
import requests

if __name__ == "__main__":
    """
        request user info & store in dictionary
    """

    request_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = request_users.json()
    list_of_users = {}
    for i in range(1, len(users) + 1):
        request_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(i))
        user = json.loads(request_employee.text)
        username = user.get("username")

        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(i))
        tasks = {}
        user_todos = request_todos.json()
        for dictionary in user_todos:
            tasks.update(
                {dictionary.get("title"): dictionary.get("completed")})

        task_list = []
        for k, v in tasks.items():
            task_list.append({
                "username": username,
                "task": k,
                "completed": v,
            })
        list_of_users[i] = task_list
        """
            export to JSON
        """

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(list_of_users, file)
