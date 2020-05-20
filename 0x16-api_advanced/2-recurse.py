#!/usr/bin/python3
""" ecursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """returns all title list hot articles for a given subreddit."""
    url = 'https://www.reddit.com'
    path = '/r/{}/hot.json?after='.format(subreddit)
    header = {'user-agent': 'jormao'}
    r = get(url + path + str(after), headers=header, allow_redirects=False)
    if (r.status_code in [302, 404]):
        return(None)
    else:
        hot_post = r.json()['data']['children']
        for hot in hot_post:
            hot_list.append(hot['data']['title'])
        after = r.json()['data']['after']
        if (after is None):
            return (hot_list)
        return recurse(subreddit, hot_list, after)
