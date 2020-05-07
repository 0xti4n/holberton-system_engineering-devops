#!/usr/bin/python3
"""queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Search number of suscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-agent': ''}

    r = requests.get(url, headers=header)
    if r.status_code == 404:
        return 0

    data = r.json()
    for k, v in data.items():
        if 'data' in k:
            return v['subscribers']
