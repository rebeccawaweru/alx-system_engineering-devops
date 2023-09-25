#!/usr/bin/python3
"""Exporting data in CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    em = requests.get(url + "users/{}".format(uid)).json()
    emname = em.get("username")
    lst = requests.get(url + "todos", params={"userId": uid}).json()

    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [uid, emname, t.get("completed"), t.get("title")]
        ) for t in lst]
