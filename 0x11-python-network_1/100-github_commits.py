#!/usr/bin/python3

"""
Print all commits by a user
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    r = r.json()
    for i in r[:10]:
        print("{}: ".format(i.get('sha')), end="")
        print("{}".format(i.get('commit').get('author').get('name')))
