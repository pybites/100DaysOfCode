import os
import re
import sys
import urllib.request

HTML = 'authors.html'
SITE = 'http://pybit.es'
URL = '{}/{}'.format(SITE, HTML)
TEST_FLAG = '-t'

args = sys.argv[1:]
author_regex = re.compile(
    r'<a href="%s/author/(.*?).html">\w+</a>\s\((\d+)\)'
    % SITE)


def download_page():
    if TEST_FLAG in args and os.path.isfile(HTML):
        print('Test mode, using cached html file')
    else:
        print('Retrieving fresh copy from authors page')
        urllib.request.urlretrieve(URL, HTML)


def get_posts():
    with open(HTML) as f:
        return {k: int(v) for k, v in author_regex.findall(f.read())}


if __name__ == '__main__':
    download_page()
    authors = get_posts()
    total = sum(authors.values())
    fmt = 'Total number of posts on {}: {}'
    print(fmt.format(SITE, total))
