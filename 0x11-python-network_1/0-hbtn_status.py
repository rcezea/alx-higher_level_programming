#!/usr/bin/python3
# Fetch a website

import urllib.request
''' This module is used to fetch html content'''

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
print("\t- utf8 content: {}".format(content.decode('utf-8')))
