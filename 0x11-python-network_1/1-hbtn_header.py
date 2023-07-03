#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request, and displays
the value of the X-Request-Id variable found in the header
"""
from urllib import request
import sys 

if __name__ == "__main__":
    req = request.Request(sys.argv[1], method='HEAD')
    with request.urlopen(req) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
