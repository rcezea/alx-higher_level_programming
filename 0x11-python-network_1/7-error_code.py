#!/usr/bin/python3
"""
Display error codes
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except Exception:
        print("Error code:", r.status_code)
