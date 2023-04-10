#!/usr/bin/python3
''' This module is used to fetch html content'''

if __name__ == '__main__':
    import urllib.request as re

    with re.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
