#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def recurse(subreddit, list=[], after='', count=0):
    """function"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    user_agent = {'User-agent': 'Python/requests'}
    params = {'after': after, 'limit': 100, 'count': count}
    req = requests.get(url, headers=user_agent,
                       params=params, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        children = data.get("children")
        for title in children:
            list.append(title.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, list, after, count)
        return list
    return None
