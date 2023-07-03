#!/usr/bin/python3
"""
This script handles HHTP errors.It takes URL, sends a request and displays
the value of the X-Request-Id variable found in the header.
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            BodyContent = response.read()
            print(BodyContent.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
