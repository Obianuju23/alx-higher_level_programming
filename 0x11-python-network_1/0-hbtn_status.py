#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        BodyContent = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(BodyContent)))
        print("\t- content: {}".format(BodyContent))
        print("\t- utf8 content: {}".format(BodyContent.decode('utf-8')))
