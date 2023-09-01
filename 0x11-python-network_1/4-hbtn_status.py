#!/usr/bin/python3
"""Fetches "https://alx-intranet.hbtn.io/status" using only requests"""

if __name__ == "__main__":
    from requests import get

    req = get('https://intranet.hbtn.io/status')
    print(f"Body response:")
    print(f"    - type: {type(req.text)}")
    print(f"    - content: {req.text}")
