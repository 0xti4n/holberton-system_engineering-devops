#!/usr/bin/python3
"""returns all information about his/her todo list progress in json"""
import json
import requests

if __name__ == "__main__":
    user = 'https://jsonplaceholder.typicode.com/users/'
    r2 = 'https://jsonplaceholder.typicode.com/todos'

    r_user = requests.get(user)
    r2 = requests.get(r2)

    data_user = r_user.json()
    data_route2 = r2.json()

    new = {}
    for user in data_user:
        new[user['id']] = []
        for i in data_route2:
            if i['userId'] == user['id']:
                new[user['id']].append({
                    'task': i['title'],
                    'completed': i['completed'],
                    'username': user['username']
                    })

    concat = 'todo_all_employees' + '.json'
    with open(concat, mode='w') as data:
        json.dump(new, data)
