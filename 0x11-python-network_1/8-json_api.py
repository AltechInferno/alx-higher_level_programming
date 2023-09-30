#!/usr/bin/python3
"""script takes in a letter and sends a post request
to http://0.0.0.0:5000/search_user with letter param
"""

import urllib.request
import sys

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': query}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data, method='POST')

    try:
        with urllib.request.urlopen(request) as response:
            x_request_id = response.headers.get('X-Request-Id')
            response_content = response.read().decode('utf-8')

        print('X-Request-Id:', {x_request_id})
        print(response_content)
    except Exception as e:
        print(f'An error occurred: {e}')

