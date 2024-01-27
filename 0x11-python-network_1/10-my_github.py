#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github.v3+json"}
    auth = {'username': username, 'password': password}
    try:
        response = requests.get(url, auth=auth, headers=headers)
        response_json = response.json()

        if response.status_code == 200:
            user_id = response_json.get('id', 'N/A')
            print(f"GitHub user id: {user_id}")
        elif response.status_code == 401:
            print("Unauthorized. Check your credentials.")
        else:
            print(f"Error: {response.status_code}")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"An error occurred: {e}")
