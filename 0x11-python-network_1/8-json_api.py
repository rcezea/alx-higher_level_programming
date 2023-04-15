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
        r = requests.post(url, data=q)
        obj = r.json
        print("[{}] {}".format(obj["id"], obj["name"]))
    else:
        q = ""
        print("No result")

    r = requests.post(url, data=q)
    print(r.json)
