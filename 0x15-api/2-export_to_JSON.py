#!/usr/bin/python3
"""returns information about his/her todo list progress in json"""
from sys import argv
import json
import requests

if __name__ == "__main__":
    av = argv[1]

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(av)
    r2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(av)

    r_user = requests.get(user)
    r2 = requests.get(r2)

    data_user = r_user.json()
    data_route2 = r2.json()

    name = data_user['username']
    user_id = data_user['id']

    new = {}
    new[user_id] = []
    for i in data_route2:
        new[user_id].append({
            'task': i['title'],
            'completed': i['completed'],
            'username': name
            })
    concat = av + '.json'
    with open(concat, mode='w') as data:
        json.dump(new, data)
