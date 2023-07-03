#!/usr/bin/python3
"""
Script that takes in a URL, sends a POST request to the passed URL,
takes email as a parameter, and displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    """makes this part of the code not to be executed"""
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email)
    data = data.encode('ascii')  #This changes the data to bytes
    request = Request(url, data)
    with urlopen(request) as response:
        BodyContent = response.read()
    print(BodyContent.decode('utf-8'))
