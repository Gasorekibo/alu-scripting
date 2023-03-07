#!/usr/bin/python3
"""
Finding hot top 10 post
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Myapi-app'}

    r = requests.get(url+'?limit=10', headers=headers)
    if r.status_code == 200:
        value = r.json()
        datas = value['data']['children']
        for each in datas:
            title = each['data']['title']
            print(title)
    else:
        print('None')
