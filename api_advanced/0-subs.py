#!/usr/bin/python3
"""
Return the number of subscribers
from any subreddit given
"""
import requests


def number_of_subscribers(subreddit):
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}
    r = requests.get(url, headers=headers).json()
    if r.status_Code == 200:
        return r['data']['subscribers']
    else:
        return 0
