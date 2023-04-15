#!/usr/bin/python3
"""
- Take in a url
- Sends a request to the url
- displays the value of the X-Request-Id
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
