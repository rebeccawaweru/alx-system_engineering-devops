#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    em = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            u.get("id"): [{
                "task": x.get("title"),
                "completed": x.get("completed"),
                "username": u.get("username")
            } for x in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in em}, json_file)
