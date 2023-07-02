#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main __':
    import urllib.request

     url = 'https://alx-intranet.hbtn.io/status'

     req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
    body_content = response.read().decode('utf-8')

print('Body response:')
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body_content))
print("\t- utf8 content: {}".format(body_content.decode("utf-8")))
