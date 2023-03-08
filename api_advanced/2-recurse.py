#!/usr/bin/python3
"""
making a recursive function
"""
import requests


def recurse(subreddit, hot_list=[]):
    
    def requesting(url):
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'User-Agent': 'Myapi-app'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            result = r.json()
            data = result['data']['children']
            for title in data:
                hot_list.append(title['data']['title'])
            after = result['data']['after']
            if after is None:
                return None
            else:
                return(requesting(after))
        return None
    
    return hot_list