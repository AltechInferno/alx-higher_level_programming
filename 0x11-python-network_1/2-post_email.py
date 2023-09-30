#!/usr/bin/python3
"""script that takes in a URL and an email, 
sends a POST request to the passed URL
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    data = {"email": argv[2]}
    request = Request(
            argv[1], urlencode(data).encode("ascii"))
    with urlopen(request) as res:
        x_request_id = res.headers.get('X-Request-Id')
        print(res.read().decode('utf-8'))
