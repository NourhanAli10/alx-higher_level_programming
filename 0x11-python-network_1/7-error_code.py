#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""
import requests
import sys

if __name__ == "__main__":
    Url = sys.argv[1]
    response = requests.get(Url)
    print(response.text)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
