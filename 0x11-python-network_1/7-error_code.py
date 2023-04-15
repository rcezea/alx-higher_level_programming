#!/usr/bin/python3
"""
Display error codes
"""

if __name__ == '__main__':

    from requests.exceptions import HTTPError
    import requests 
    import sys

    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
    except HTTPError as e:
        print("Error code: ", e.errno)
