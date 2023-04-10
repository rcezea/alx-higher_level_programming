#!/usr/bin/python3
# Fetch a website

import urllib.request
''' This module is used to fetch html content'''

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
string = f"Body response:\n\
    \t- type: {type(html)}\n\
    \t- content: {html}\n\
    \t- utf8 content: {html.decode('utf-8')}"
print(string)