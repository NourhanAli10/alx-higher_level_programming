#!/bin/bash
# Check if the URL is provided as an argument

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request and display the body only for a 200 status code
response=$(curl -s -w "%{http_code}" "$url")

# Extract the status code
status_code=$(tail -c 3 <<< "$response")

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
    # Display the body of the response
    body=$(curl -s "$url")
    echo "Response body:"
    echo "$body"
else
    echo "Received a non-200 status code: $status_code"
fi
