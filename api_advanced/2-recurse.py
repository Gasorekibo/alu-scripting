#!/usr/bin/python3
"""
python scrip that uses recursive function to 
retrieve all post title and store them in 
a list in our case it is hot_list
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    subreddit_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Myapi-app'}
    parameter = {'after':after}

    r = requests.get(subreddit_url, headers=headers,params=parameter,
                     allow_redirect=False)
    
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
