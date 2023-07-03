#!/usr/bin/python3
"""
This script takes a URL sends a request to the URL&displays the body of the
response then displays the HTTP status code if greater than or equal 400
"""
if __name__ == '__main__':
    from sys import argv 
    import requests

    url = argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
