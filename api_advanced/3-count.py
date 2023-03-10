#!/usr/bin/python3
"""
Recursively queries the Reddit API to get the title of all
hot articles for a given subreddit and count the number of
occurrences of each keyword in the titles.
"""
import requests


def get_hot_posts(keyword_list, subreddit='all', limit=100, after=None, count=0, posts={}):
    """
    Recursively queries the Reddit API to get the title of all hot articles for a given subreddit and count the number of
    occurrences of each keyword in the titles.
    
    :param keyword_list: A list of keywords to search for (case-insensitive, delimited by spaces).
    :param subreddit: The subreddit to search (default is 'all').
    :param limit: The maximum number of posts to retrieve per request (default is 100).
    :param after: The 'after' parameter for pagination (default is None).
    :param count: The total number of posts retrieved so far (default is 0).
    :param posts: A dictionary containing the count of each keyword found so far (default is {}).
    :return: A dictionary containing the count of each keyword found in the titles of the hot posts.
    """
    # Build the URL for the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    if after:
        url += f"&after={after}"
    
    # Set the user-agent header to avoid being blocked by the API
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Send the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts_data = data['data']['children']
        
        # Process the posts
        for post_data in posts_data:
            title = post_data['data']['title'].lower()
            for keyword in keyword_list:
                if keyword.lower() in title and (' '+keyword.lower()+' ' in title
                                                 or title.startswith(keyword.lower()+' ')
                                                 or title.endswith(' '+keyword.lower())):
                    if keyword not in posts:
                        posts[keyword] = 1
                    else:
                        posts[keyword] += 1
        
        # Check if there are more posts to retrieve
        if data['data']['after'] and count < limit:
            count += len(posts_data)
            get_hot_posts(keyword_list, subreddit, limit, data['data']['after'], count, posts)
    
    # Print the count of each keyword found
    for keyword in sorted(posts):
        print(f"{keyword}: {posts[keyword]}")
    
    # Return the count of each keyword found
    return posts