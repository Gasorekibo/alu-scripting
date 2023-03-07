#!/usr/bin/python3
"""
    Return the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'Myapi-app'}
        r = requests.get(url, headers=headers).json()
        return r['data']['subscribers']
    except:
        return None
