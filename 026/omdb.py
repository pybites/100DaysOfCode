from pprint import pprint as pp
import sys

import requests
import requests_cache

from templates import TEMPLATE, HTML_TEMPLATE

OMDB = 'http://www.omdbapi.com'
OMDB_BY_IMDB = OMDB + '/?i={imdb}'
OMDB_BY_TITLE_YEAR = OMDB + '/?t={title}&y={year}'

# cache repeated calls to OMDB (not sure about API limits)
requests_cache.install_cache()


def query_omdb(**kwargs):
    if 'imdb' in kwargs:
        url = OMDB_BY_IMDB.format(**kwargs)
    else:
        url = OMDB_BY_TITLE_YEAR.format(**kwargs)
    return requests.get(url).json()


if __name__ == '__main__':
    args = sys.argv[1:]
    html = True if '-h' in args else False
    verbose = True if '-v' in args else False
    answer = None

    print('Script to query OMDb API')

    while answer != 'q':
        answer = input('Enter IMDB ID or title (q to exit): ').lower()
        params = dict()

        if answer == 'q':
            print('Bye')
            break
        elif 'tt' in answer:
            params['imdb'] = answer
        else:
            params['title'] = answer
            params['year'] = input('Year of release? ')

        resp = query_omdb(**params)
        if verbose: 
            pp(resp)

        if 'Error' in resp:
            print('Error: {}'.format(resp['Error']))
        else:
            tmpl = HTML_TEMPLATE if html else TEMPLATE
            print(tmpl.format(**dict(resp)))
