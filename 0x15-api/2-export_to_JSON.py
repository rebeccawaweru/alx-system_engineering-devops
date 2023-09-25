#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    em = requests.get(url + "users/{}".format(uid)).json()
    emname = em.get("username")
    lst = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.json".format(uid), "w") as json_file:
        json.dump({uid: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": emname
            } for t in lst]}, json_file)
