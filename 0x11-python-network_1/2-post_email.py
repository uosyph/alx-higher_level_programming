#!/usr/bin/python3
"""Sends a POST request to a given URL and an email,
then displays the response"""


if __name__ == "__main__":
    from sys import argv
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

    value = {'email': argv[2]}
    data = urlencode(value)
    data = data.encode('ascii')

    req = Request(argv[1], data)
    with urlopen(req) as res:
        print(str(res.read(), 'utf-8'))
