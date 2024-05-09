#!/usr/bin/python3
"""A recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    if 'children' in data['data']:
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list
    else:
        return hot_list
