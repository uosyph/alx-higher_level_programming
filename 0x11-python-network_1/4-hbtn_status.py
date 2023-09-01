#!/usr/bin/python3
"""Fetches "https://alx-intranet.hbtn.io/status" using only requests"""

if __name__ == "__main__":
    from requests import get

    req = get('https://intranet.hbtn.io/status')
    print(f"Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
