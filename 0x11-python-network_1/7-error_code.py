#!/usr/bin/python3
"""Sends a request to a given URL using requests,
then displays the error code"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    req = get(argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
