#!/usr/bin/python3
"""
Display error codes
"""

if __name__ == '__main__':

    import urllib.request
    from urllib.error import HTTPError
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
