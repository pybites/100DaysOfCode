#!python3
#pull_xml.py uses the requests module to pull down the feed xml file for use in an external xml parser script.
#This will result in just one call/request to the specified webserver hosting this XML file.

import requests

URL = ""

if __name__ == "__main__":
	r = requests.get(URL)
	with open('your_file_name.xml', 'wb') as f:
		f.write(r.content)
