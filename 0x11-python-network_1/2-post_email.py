#!/usr/bin/python3
""" A script that
- takes in a URL and an email
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':

    import urllib.request
    import urllib.parse
    import sys

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode()
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
