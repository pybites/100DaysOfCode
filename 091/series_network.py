from __future__ import print_function

import os
from pprint import pprint as pp
import sys

from tvdb_client import ApiV2Client

user = os.environ.get('TVDB_USER')
api_key = os.environ.get('TVDB_APIKEY')
acc_ident = os.environ.get('TVDB_IDENT')
if not user or not api_key or not acc_ident:
    print('set user, api_key and acc_ident in env')
    sys.exit(1)

# https://github.com/thilux/tvdb_client/issues/1
# only works on python 2!!
api_client = ApiV2Client(user, api_key, acc_ident)
api_client.login()

if not api_client.is_authenticated:
    print('not authenticated')
    sys.exit(1)

if len(sys.argv) < 2:
    search = raw_input('Search for series: ')
else:
    search = " ".join(sys.argv[1:])

resp = api_client.search_series(name=search)
if 'code' in resp and resp['code'] != 200:
    print('{} response from API'.format(resp['code']))
    sys.exit(1)

# pp(resp)
info = '''
    Name:       {name}
    Network:    {network}
    Overview:   {overview}
'''.format(name=resp['data'][0]['seriesName'].encode('utf-8'),
           network=resp['data'][0]['network'].encode('utf-8'),
           overview=resp['data'][0]['overview'].encode('utf-8'),
           status=resp['data'][0]['status'].encode('utf-8'))

print(info)
