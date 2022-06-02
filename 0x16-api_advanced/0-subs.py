#!/usr/bin/python3
"""returns the number of subscribers from Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """function"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    user_agent = {'User-agent': 'Python/requests'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
