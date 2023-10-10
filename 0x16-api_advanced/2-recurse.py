#!/usr/bin/python3
""" Function that prints top 10 posts for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Get hot posts
        Args:
            subreddit: name of subreddit
            host_list: title list
            after: next results id
    """
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    hot_dict = hot_list + [child.get("data").get("title")
                           for child in response.json()
                           .get("data")
                           .get("children")]
    info = response.json()
    if not info.get("data").get("after"):
        return hot_dict

    return recurse(subreddit, hot_dict, info.get("data").get("count"),
                   info.get("data").get("after"))
