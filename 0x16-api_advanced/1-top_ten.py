#!/usr/bin/python3
""" unction that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """ rints the titles of the first 10 hot posts"""
    url = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    header = {'user-agent': 'jormao'}
    r = get(url + path, headers=header).json()
    if (r.get('error')):
        return (0)
    hot_post = r['data']['children']
    count = 0
    for hot in hot_post:
        if (count < 10):
            print(hot['data']['title'])
        count += 1
