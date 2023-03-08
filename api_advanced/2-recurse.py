#!/usr/bin/python3
"""
recursive
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    subreddit_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}
    parameter = {'after': after}

    r = requests.get(subreddit_url, headers=headers, params=parameter,
                     allow_redirects=False)
    if r.status_code == 200:
        datas = r.json()
        values = datas['data']['children']

        for each in values:
            title = each['data']['title']
            hot_list.append(title)
        after = datas['data']['after']

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
