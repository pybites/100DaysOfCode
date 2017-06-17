import os
import re
import sys
import time
import urllib.request

HTML = 'authors.html'
NOW = int(time.time())
SECONDS_IN_HOUR = 60*60
SITE = 'https://pybit.es'
URL = '{}/{}'.format(SITE, HTML)

args = sys.argv[1:]
author_regex = re.compile(
    r'<a href="%s/author/(.*?).html">\w+</a>\s\((\d+)\)'
    % SITE)


def download_page(test=False):
    print('Getting authors page which lists number of posts per author')
    if test:
        print('Test mode, using cached html file')
    elif (NOW - os.stat(HTML).st_ctime) < SECONDS_IN_HOUR:
        print('Cache file less than an hour old, using it')
    else:
        print('Not test mode nor cache file expired, retrieving fresh copy')
        urllib.request.urlretrieve(URL, HTML)


def get_posts():
    with open(HTML) as f:
        return {k: int(v) for k, v in author_regex.findall(f.read())}


if __name__ == '__main__':
    test = '-t' in sys.argv[1:]
    download_page(test)

    authors = get_posts()

    total = sum(authors.values())

    fmt = 'Total number of posts on {}: {}'
    print(fmt.format(SITE, total))
