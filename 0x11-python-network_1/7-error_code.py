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
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print("Error code: ", r.status_code)
