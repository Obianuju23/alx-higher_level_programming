#!/usr/bin/python3
"""
Script that takes in a URL, sends a POST request to the passed URL,
takes email as a parameter, and displays the body of the response
"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
