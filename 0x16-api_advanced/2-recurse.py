#!/usr/bin/python3
"""
this script contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a
given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ The querying recursive function"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'API Agent'}
    params = {'after': after} if after else None
    response = requests.get(url, headers=headers, params=params)

    # check whether the response is OK
    if response.status_code != 200:
        return None

    # process the response data
    data = response.json()
    children = data.get("data").get("children")
    for child in children:
        hot_list.append(child.get("data").get("title"))

    # check for more pages
    after = data.get("data").get("after")
    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
