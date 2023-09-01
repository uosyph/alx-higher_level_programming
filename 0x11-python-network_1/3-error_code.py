#!/usr/bin/python3
"""Sends a request to a given URL, then displays the error code"""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(str(response.read(), 'utf-8'))
    except HTTPError as err:
        print(f"Error code: {err.getcode()}")
