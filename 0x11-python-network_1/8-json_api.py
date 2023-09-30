#!/usr/bin/python3
"""script takes in a letter and sends a post request
to http://0.0.0.0:5000/search_user with letter param
"""
if __name__ == "__main__":
    from requests import post
    from sys import argv
    
    url = 'http://0.0.0.0:5000/search_user'
    query = argv[1] if len(argv) > 1 else ""
    data={'q':query}
    req = post(url, data)
    try:
        response = req.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print('Not a valid JSON')
