#!/usr/bin/python3
"""
making a recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=None,count = 0):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}
    parameter = {'after': after}
    r = requests.get(url+"?limit=100", headers=headers, param=parameter)
    if r.status_code == 200:
        data = r.json()
        results = data['data']['children']
        for each in results:
            hot_list.append(each['data']['title'])
        
        after = data['data']['after']
        if after is None:
            return hot_list
        count += 1
        return recurse(subreddit, after=after,
                           hot_list=hot_list, count=count)
    return None
if __name__ == '__main__':
    print(recurse("zerowastecz"))
