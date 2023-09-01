#!/usr/bin/python3
"""Sends a POST request to a given URL and an email using requests,
then displays the response"""

if __name__ == "__main__":
    from sys import argv
    from requests import post

    req = post(argv[1], data={'email': argv[2]})
    print(req.text)
