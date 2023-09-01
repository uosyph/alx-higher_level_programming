#!/usr/bin/python3
"""Sends a GET request to a given URL,
then displays the value of X-Request-Id in the response header"""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as res:
        html = res.info()

    print(html.get('X-Request-Id'))
