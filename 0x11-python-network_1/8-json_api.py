#!/usr/bin/python3

"""
Takes in a letter
Sends a post request to http://0.0.0.0:5000/search_user
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = {'q': sys.argv[1]}
    else:
        q = ""

    r = requests.post(url, data=q)
    try:
        obj = r.json()
        if not obj:
            print("No result")
            exit(1)
        print("[{}] {}".format(obj["id"], obj["name"]))
    except Exception:
        print("Not a valid JSON")
