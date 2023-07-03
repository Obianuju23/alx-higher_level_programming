#!/usr/bin/python3
"""
This script that takes your github credentials,Uses the Github API
to display your id
"""
from sys import argv
import requests


if __name__ == "__main__":
    """stops the code from being executed when imported"""
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    credentials = (username, password)
    res = requests.get(url, auth=credentials)
    res = res.json()
    print(res.get('id'))
