#!/usr/bin/python3
"""
3-count.py
"""
import json
import requests


def count_words(subreddit, word_list, limit=100, after=None, count=0, posts={}):
    """ prints a sorted count of given keywords """
    url = "https://www.reddit.com/r/{}/hot.json?limit={limit}".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts_data = data['data']['children']
        for post_data in posts_data:
            title = post_data['data']['title'].lower()
            for keyword in word_list:
                if keyword.lower() in title and (' '+keyword.lower()+' ' in title or title.startswith(keyword.lower()+' ') or title.endswith(' '+keyword.lower())):
                    if keyword not in posts:
                        posts[keyword] = 1
                    else:
                        posts[keyword] += 1
        if data['data']['after'] and count < limit:
            count += len(posts_data)
            count_words(word_list, subreddit, limit, data['data']['after'], count, posts)
    for keyword in sorted(posts):
        print(f"{keyword}: {posts[keyword]}")
    
    return posts
