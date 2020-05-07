#!/usr/bin/python3
""" ecursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
"""
from requests import get


def count_words(subreddit, word_list, after="", counter={}, first=0):
    """parses the title of all hot articles, and prints a sorted list."""
    url = 'https://www.reddit.com'
    path = '/r/{}/hot.json?after='.format(subreddit)
    header = {'user-agent': 'jormao'}
    r = get(url + path + str(after), headers=header, allow_redirects=False)
    if (first == 0):
        for word in word_list:
            counter[word] = 0
        first = 1
    if (r.status_code in [302, 404]):
        return(None)
    else:
        hot_post = r.json()['data']['children']
        for hot in hot_post:
            new_list = (hot['data']['title']).lower().split(" ")
            for word in word_list:
                for w_list in new_list:
                    if word == w_list:
                        counter[word] += 1
        after = r.json()['data']['after']
        if (after is not None):
            count_words(subreddit, word_list, after, counter, first)
        else:
            p = sorted(counter.items(), key=lambda x: x[1], reverse=True)
            for k, v in p:
                if v != 0:
                    print('{}: {}'.format(k, v))
