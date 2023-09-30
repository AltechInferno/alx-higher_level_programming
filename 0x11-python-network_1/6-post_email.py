#!/usr/bin/python3
"""takes a url and an email address, sends a
post request to the passed url with the email
"""


if __name__ == "__main__":
    from requests import post
    from sys import argv
    
    data = data={'email': argv[2]}
    req = post(argv[1], data)
    print(req.text)
