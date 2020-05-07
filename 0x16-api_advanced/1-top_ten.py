#!/usr/bin/python3
"""queries the Reddit API and prints
the titles of the first 10 hot posts
listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """queries 10 post"""
    url = 'https://www.reddit.com/r/{}/hot'.format(subreddit)
    queri = url + '.json?limit=10'
    header = {'User-agent': ''}

    r = requests.get(queri, headers=header)
    if r.status_code == 404:
        print(None)
    else:
        titles = r.json()

        for indx in titles['data']['children']:
            print(indx['data']['title'])
