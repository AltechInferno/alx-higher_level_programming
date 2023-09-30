#!/usr/bin/python3
"""takes in a url, sends a request to the url 
and displays the value of the variable x-request-id
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    req = get(argv[1])
    x_request_id = req.headers.get('X-Request-Id')
    print(x_request_id)
