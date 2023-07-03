#!/usr/bin/python3
"""
This is a module that takes in a URL,Sends a request to the URL and
Displays the Value of the X-Request-Id Variable
"""
import requests
from sys import argv


if __name__ == "__main__":
    """This code cannot be executed when imported"""
    res = requests.get(argv[1])
    value = res.headers.get("X-Request-Id")
    print(value)
