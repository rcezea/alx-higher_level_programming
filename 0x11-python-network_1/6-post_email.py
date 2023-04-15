#!/usr/bin/python3
""" A script that
- takes in a URL and an email
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':

    import requests
    import sys

    email = {"email": sys.argv[2]}
    url = sys.argv[1]

    r = requests.post(url, data=email)
    print(r.text)
