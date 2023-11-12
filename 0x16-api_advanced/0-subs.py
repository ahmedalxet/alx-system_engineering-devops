#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    # Set the custom User-Agent header
    headers = {"User-Agent": "reddit_api/0.0.1"}
    
    # Make a GET request to the subreddit's about.json endpoint
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers
    )
    
    # Check the status code and the data type of the response
    if (
        response.status_code == 200 and 
        response.headers["content-type"] == "application/json; charset=UTF-8"
    ):
        # Parse the JSON data
        data = response.json()
        
        # Return the number of subscribers from the data
        return data["data"]["subscribers"]
    
    else:
        # Return 0 for invalid subreddit
        return 0
