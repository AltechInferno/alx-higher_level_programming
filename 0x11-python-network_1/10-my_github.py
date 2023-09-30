#!/usr/bin/python3
"""takes Github creds and uses the github api to display
your id
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv
    
    url = 'https://api.github.com/user'
    auth = (argv[1], argv[2])
    req = get(url, auth=auth)
    results = req.json().get('id')
    print(results)
