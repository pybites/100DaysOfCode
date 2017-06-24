#!python3
#currency_converter.py converts one currency to another.

import requests
import json

#API_URL = "https://openexchangerates.org/api/convert/{}/{}/{}?app_id=".format(amount, from_curr, to_curr)
API_KEY = "YOUR_PREMIUM_APP_ID_HERE"

def user_input():
    print("Valid currencies are listed in included currencies.txt file.")
    amount = str(input("Please enter the amount: "))
    from_curr = input("Please enter the currency to convert FROM: ")
    to_curr = input("Please enter the currency to convert TO: ")
    data = [amount, from_curr, to_curr]
    return data

def api_request(data):
    api_url = ("https://openexchangerates.org/api/convert/{}/{}/{}?app_id=".format(data[0], data[1], data[2]) + API_KEY)
    return requests.get(api_url).json()
    
if __name__ == "__main__":
    conversion_data = user_input()
    json_data = api_request(conversion_data)
    print("\nResult = ${}".format(json_data['response']))