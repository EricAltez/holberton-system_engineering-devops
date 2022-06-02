#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    user_agent = {'User-agent': 'Python/requests'}
    req = requests.get(url, headers=user_agent,
                       params={'limit': 10}, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get("data")
        children = data.get("children")
        for title in children:
            print(title.get('data').get('title'))
    else:
        print("None")
