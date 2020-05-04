#!/usr/bin/python3
"""returns information about his/her todo list progress in cvs """
import requests
from sys import argv
import csv

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

    with open(av + '.csv', 'w', newline='') as data:
        writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in data_route2:
            writer.writerow([user_id, name, i['completed'], i['title']])
