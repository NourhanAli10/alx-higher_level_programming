#!/bin/bash
# Bash script that takes in a URL, sends a request to that URl
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n'
