#!/usr/bin/python3
"""Sends a POST request to "http://0.0.0.0:5000/search_user"
with a given letter as a parameter"""

if __name__ == "__main__":
    from sys import argv
    from requests import post

    if len(argv) == 1:
        let = ""
    else:
        let = argv[1]

    req = post("http://0.0.0.0:5000/search_user", data={"q": let})
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print(f'[{res.get("id")}] {res.get("name")}')
    except ValueError:
        print("Not a valid JSON")
