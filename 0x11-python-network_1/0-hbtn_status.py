#!/usr/bin/python3
import urllib.request

def fetch_status(url):
    """
    Fetches the status from the given URL using urllib.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        dict: A dictionary containing the type, content, and utf8 content of the response.
    """
    with urllib.request.urlopen(url) as response:
        html = response.read()
        utf8_content = html.decode('utf-8')
        return {
            "type": type(html),
            "content": html,
            "utf8_content": utf8_content
        }

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    status_info = fetch_status(url)

    print("Body response:")
    for key, value in status_info.items():
        print(f"\t- {key}: {value}")
