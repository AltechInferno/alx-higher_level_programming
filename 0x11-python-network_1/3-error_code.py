#!/usr/bin/python3
"""a script that takes in a url, sends a 
request to the url and displays body of 
response decoded in utf-8
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        url = argv[1]
        with urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)
