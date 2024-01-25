#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays size of the body of the response.
curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r'

