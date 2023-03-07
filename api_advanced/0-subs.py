#!/usr/bin/python3
"""
Return the number of subscribers
from any subreddit given
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        value = r.json()
        return value['data']['subscribers']
    return 0
