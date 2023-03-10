#!/usr/bin/python3
"""
counting word occurence
"""
import requests


def count_words(subreddit, word_list, after=None, count=0, posts={}, limit=100):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    if after:
        url += f"&after={after}"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts_data = data['data']['children']
        
        for post_data in posts_data:
            title = post_data['data']['title'].lower()
            for keyword in word_list:
                if keyword.lower() in title and (' '+keyword.lower()+' ' in title
                                                 or title.startswith(keyword.lower()+' ')
                                                 or title.endswith(' '+keyword.lower())):
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