#!/usr/bin/python3
''' This module is used to fetch html content'''

if __name__ == '__main__':
    import urllib.request as re

    with re.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    string = f"Body response:\n\
        - type: {type(html)}\n\
        - content: {html}\n\
        - utf8 content: {html.decode('utf-8')}"
    print(string)
