import os
from pprint import pprint as pp
import sys

import tvdbsimple as tvdb

api_key = os.environ.get('TVDB_APIKEY') or sys.exit('set api key in env')
tvdb.KEYS.API_KEY = api_key

search = tvdb.Search()
reponse = search.series("mr robot")
first_hit = search.series[0]
pp(first_hit)

showid = first_hit['id']
show = tvdb.Series(showid)

episodes = show.Episodes.all()
pp(episodes)
