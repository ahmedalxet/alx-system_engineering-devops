#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "RedditBot"}

    # Add 'after' parameter to the URL if it is not None
    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get("data", {}).get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        hot_list.append(title)

    # Recursive call with the 'after' parameter set to the value of 'name' in the last child
    after = data.get("data", {}).get("after")
    if after:
        return recurse(subreddit, hot_list, after=after)

    return hot_list
