#!/usr/bin/python3
"""
- Take in a url
- Sends a request to the url
- displays the value of the X-Request-Id
"""
if __name__ == '__main__':
    import urllib.request as re
    import sys

    with re.urlopen(sys.argv[1]) as res:
        content = res.getheader('X-Request-Id')
    print(content)
