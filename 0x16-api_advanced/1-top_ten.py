#!/usr/bin/python3
""" Printing top ten host posts for a given subreddit """
import requests


def top_ten(subreddit):
    """ Get top 10 posts in subreddit
        Args:
            subreddit: name of subreddit
    """
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?limit=10'.format(
            url, subreddit), headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
    else:
        dict_hot = response.json()
        if len(dict_hot['data']['children']) == 0:
            print('None')
        else:
            for x in dict_hot['data']['children']:
                print(x['data']['title'])
