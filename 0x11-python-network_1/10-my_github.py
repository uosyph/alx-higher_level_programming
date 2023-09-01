#!/usr/bin/python3
"""Takes your GitHub credentials and uses the GitHub API to display your id"""

if __name__ == "__main__":
    from sys import argv
    from requests import get
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(argv[1], argv[2])
    res = get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
