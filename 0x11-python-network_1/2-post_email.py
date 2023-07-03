#!/usr/bin/python3
"""
Script that takes in a URL,sends a POST request to the passed URL,
takes email as a parameter&displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data =  parse.urlencode({"email": email}).encode("ascii")

    req = request.Request(url, data=data, method="POST")
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
