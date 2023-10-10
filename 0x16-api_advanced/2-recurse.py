#!/usr/bin/python3
""" Function that prints top 10 posts for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Get hot posts
        Args:
            subreddit: name of subreddit
            host_list: title list
            after: next results id
    """
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?after={}'.format(
            url, subreddit, after), headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        dict_hot = response.json()
        if len(dict_hot['data']['children']) == 0:
            return hot_list
        else:
            for x in dict_hot['data']['children']:
                hot_list.append(x['data']['title'])
            after = dict_hot['data']['after']
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after=after)
