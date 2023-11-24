#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse the titles of all hot articles,
and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list):
    count_dict = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        for article in articles:
            title = article["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    count_dict[word] = count_dict.get(word, 0) + 1

        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

        if not sorted_counts:
            print("No matching keywords found.")
    else:
        print("Invalid subreddit or no posts found.")
