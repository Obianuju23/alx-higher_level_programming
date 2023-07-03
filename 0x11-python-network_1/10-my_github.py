#!/usr/bin/python3
"""
This script that takes your github credentials,Uses the Github API 
to display your id
"""
from sys import sysargv
import requests


if __name__ == "__main__":
    """prevents from being executed when imported"""
    url = "https://api.github.com/user"
    username = sysargv[1]
    password = sysargv[2]
    credentials = (username, password)
    res = requests.get(url, auth=credentials)
    res = res.json()
    print(res.get('id'))
