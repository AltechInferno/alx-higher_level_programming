#!/usr/bin/piython3
"""solve a challenge with 2 arguments
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    req = get(url).json()
    try:
        for r in range(10):
            print("{}: {}".format(
                req[r].get("sha"),
                req[r].get("commit").get("author").get("name")))
    except IndexError:
        pass
