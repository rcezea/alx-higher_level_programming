#!/usr/bin/python3

"""
Takes in a letter
Sends a post request to http://0.0.0.0:5000/search_user
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        q = {'letter': sys.argv[1]}
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, params=q)
    print(r.json)
