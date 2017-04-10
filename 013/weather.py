from datetime import datetime
import os

import pytz
import requests

API_KEY = os.environ.get('WEATHER_API')
API_URL = ('http://api.openweathermap.org/data/2.5/weather?'
           'q={}&mode=json&units=metric&appid={}')
DEFAULT_TIME = 'Europe/Madrid'
TIME_FMT = '%H:%M:%S %Z%z'


def get_local_time(utstamp, country, city):
    utc_dt = datetime.utcfromtimestamp(int(utstamp)).replace(tzinfo=pytz.utc)

    timezones = pytz.country_timezones.get(country.upper(), [])
    closest_timezone = [tz for tz in timezones if city.lower() in tz.lower()]

    if closest_timezone:
        tz = closest_timezone[0]  # tz + city
    elif timezones:
        tz = timezones[0]  # just tz
    else:
        tz = DEFAULT_TIME  # emea

    loc_tz = pytz.timezone(tz)
    dt = utc_dt.astimezone(loc_tz)
    return dt.strftime(TIME_FMT)


def query_api(city):
    try:
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

if __name__ == '__main__':
    print(get_local_time(1491822714, 'EC', 'Quito'))
