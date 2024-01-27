#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response."""

import urllib.request as url
import sys

Url = sys.argv[1]

request = url.urlopen(Url)

with  request as response:
    print(request.headers.get("X-Request-Id"))
