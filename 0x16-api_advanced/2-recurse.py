#!/usr/bin/python3
"""queries the Reddit API and returns a
list containing the titles of all hot articles
for a given subreddit. If no results are found for
the given subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], next_page=''):
    """queries recursively hot titles"""
    url = 'https://www.reddit.com/r/{}/hot'.format(subreddit)
    queri = url + '.json?after={}'.format(next_page)
    header = {'User-agent': ''}

    r = requests.get(queri, headers=header)
    if r.status_code == 404:
        return None

    else:
        titles = r.json()
        for indx in titles['data']['children']:
            hot_list.append(indx['data']['title'])
        next_page = titles['data']['after']
        if next_page is None:
            return hot_list

        return recurse(subreddit, hot_list, next_page)
