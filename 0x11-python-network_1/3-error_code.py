#!/usr/bin/python3
"""
Display error codes
"""

if __name__ == '__main__':

    import urllib.request
    from urllib.error import HTTPError
    import sys

    try:
        with urllib.request.urlopen('http://rclancing.tech/call') as response:
            print(response.read())
    except HTTPError as e:
        print("Error code:", e.code)
