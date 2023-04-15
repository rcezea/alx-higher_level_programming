#!/usr/bin/python3
"""
Takes GitHub credentials
Uses GitHub API to display user id
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    r = requests.get(url, auth=(user, passwd))
    print(r.json().get('id'))