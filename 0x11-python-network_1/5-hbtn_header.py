#!/usr/bin/python3
"""Sends a GET request to a given URL using requests,
then displays the value of X-Request-Id in the response header"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    req = get(argv[1])
    print(req.headers.get('X-Request-Id'))
