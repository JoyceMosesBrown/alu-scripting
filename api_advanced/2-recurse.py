#!/usr/bin/python3
"""Return a list containing the titles
 of all hot articles for a given subreddit"""

import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def recurse(subreddit, after="", hot_list=[], page_counter=0):

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:
        json_data = response.json()

        for child in json_data.get('data').get('children'):
            title = child.get('data').get('title')
            hot_list.append(title)

