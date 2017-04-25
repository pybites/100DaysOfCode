#!python3
#Script to pull user data about a World of Warcraft character
#Must have an API client_id and secret_id obtained from https://dev.battle.net
#TODO: Update to allow users to select which data to pull, ie, Char Info, Guild Info, Achieve Info etc.
#TODO-2: Would be nice to strip out Item IDs/names & have them link to Wowhead.

import requests
import json
from pprint import pprint

API_KEY = ""

char_name = input('Please enter character name: ')
realm = input('Please enter realm: ')

url = ('https://us.api.battle.net/wow/character/%s/%s?fields=mounts&locale=en_US&apikey=%s' % (realm, char_name, API_KEY))

input('Hit Enter to Continue')

r = requests.get(url)

data = json.loads(r.text)

pprint(data)

#Uncomment the below code to save the data to a file as a string.
#Go easy, it's a work in progress!

#with open('output.json', 'w') as f:
#	f.write(str(data))
