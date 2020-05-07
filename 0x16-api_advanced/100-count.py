#!/usr/bin/python3
"""queries the Reddit API and returns a
list containing the titles of all hot articles
for a given subreddit. If no results are found for
the given subreddit, the function should return None."""
import requests
from collections import OrderedDict


def count_words(subreddit, word_list, next_page='', new_ditc={}):
    """queries recursively hot titles"""
    url = 'https://www.reddit.com/r/{}/hot'.format(subreddit)
    queri = url + '.json?&after={}'.format(next_page)
    header = {'User-agent': 'agent xtian'}

    r = requests.get(queri, headers=header, allow_redirects=False)
    if r.status_code == 302:
        return
    elif r.status_code == 404:
        return

    else:
        if len(new_ditc) == 0:
            new_ditc = dict.fromkeys(word_list, 0)
        concat = ''
        titles = r.json()
        for indx in titles['data']['children']:
            concat += indx['data']['title']
            all_titles = concat.split(' ')

        for indx in all_titles:
            for k, v in new_ditc.items():
                if k == indx:
                    new_ditc[k] += 1

        next_page = titles['data']['after']
        if next_page is None:
            order_dict = OrderedDict(sorted(new_ditc.items(),
                                     key=lambda x: x[1],
                                     reverse=True))
            for k, v in order_dict.items():
                if v != 0:
                    print('{}: {}'.format(k, v))

        else:
            return count_words(subreddit, word_list, next_page, new_ditc)
