#!/usr/bin/python3
"""Displays the value of X-Request-Id var found in
header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")

