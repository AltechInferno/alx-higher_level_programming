#!/usr/bin/python3
"""fetch from https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
	import urllib.request

	url = "https://alx-intranet.hbtn.io/status"

	try:
		with urllib.request.urlopen(url) as response:
			html = response.read()
			print("Body response:")
			print("\t- type: {}".format(type(html)))
			print("\t- content: {}".format(html.decode("utf-8")))
	except Exception as e:
		print("Error: {}".format(e))
