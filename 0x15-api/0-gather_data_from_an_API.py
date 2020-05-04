#!/usr/bin/python3
"""returns information about his/her todo list progress"""
from sys import argv
import requests

if __name__ == "__main__":
    av = argv[1]

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(av)
    r2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(av)

    r_user = requests.get(user)
    r2 = requests.get(r2)

    data_user = r_user.json()
    data_route2 = r2.json()

    name = data_user['name']
    con = 0
    t_task = 0
    t_done = []
    for task in data_route2:
        t_task += 1
        if task['completed'] is True:
            t_done.append(task['title'])
            con += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, con, t_task))
    for done in t_done:
        print('\t{}'.format(done))
