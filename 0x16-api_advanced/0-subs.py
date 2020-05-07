#!/usr/bin/python3
""" function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
"""
from requests import get


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""
    url = 'https://www.reddit.com'
    path = '/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'jormao'}
    r = get(url + path, headers=header).json()
    if r.get('data') and r.get('data').get('subscribers'):
        return (r['data']['subscribers'])
    return (0)
