#!/usr/bin/python3
"""Return information about employee TODO list"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    em = requests.get(url + "users/{}".format(sys.argv[1])).json()
    lst = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    complete = [c.get("title") for c in lst if c.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        em.get("name"), len(complete), len(lst)))
    [print("\t {}".format(x)) for x in complete]
