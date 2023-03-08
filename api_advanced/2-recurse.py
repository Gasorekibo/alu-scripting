#!/usr/bin/python3
# """
# making a recursive function
# """
# import requests


# def recurse(subreddit, hot_list=[], after=None,count = 0):
#     url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
#     headers = {'User-Agent': 'Myapi-app'}
#     parameter = {'after': after}
#     r = requests.get(url+"?limit=100", headers=headers, param=parameter)
#     if r.status_code == 200:
#         data = r.json()
#         results = data['data']['children']
#         for each in results:
#             hot_list.append(each['data']['title'])
        
#         after = data['data']['after']
#         if after is None:
#             return hot_list
#         count += 1
#         return recurse(subreddit, after=after,
#                            hot_list=hot_list, count=count)
#     return None
# if __name__ == '__main__':
#     print(recurse("zerowastecz"))

"""Module for recurse function"""
import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def recurse(subreddit, after="", hot_list=[], page_count=0):

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:
        json_data = response.json()

        for child in json_data.get('data').get('children'):
            title = child.get('data').get('title')
            hot_list.append(title)

        after = json_data.get('data').get('after')
        if after is not None:

            page_count += 1
            return recurse(subreddit, after=after,
                           hot_list=hot_list, page_count=page_count)
        else:
            return hot_list

    else:
        return None


if __name__ == '__main__':
    print(recurse("zerowastecz"))