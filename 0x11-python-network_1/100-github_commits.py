#!/usr/bin/python3
"""Lists the 10 most recent commits in a given repo with a given owner"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    res = get(url)
    commits = res.json()
    try:
        for commit in range(10):
            print(f'{commits[commit].get("sha")}: \
                  {commits[commit].get("commit").get("author").get("name")}')
    except IndexError:
        pass
