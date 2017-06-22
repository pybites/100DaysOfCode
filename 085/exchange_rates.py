#!python3
#exchante_rates.py is a script to list out current exchange rates for all currencies

import requests
import json

API_URL = "https://openexchangerates.org/api/latest.json?app_id="
API_KEY = "<INSERT YOUR APP ID KEY HERE>"

def get_json():
    return requests.get(API_URL + API_KEY).json()

def exchange_rates(data):
    rates = data['rates']
    print("US$1.00 currently buys:")
    for k, v in rates.items():
        print("{}: {}".format(k, v))

if __name__ == "__main__":
    data = get_json()
    exchange_rates(data)
