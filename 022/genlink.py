#!/usr/bin/env python3
import re
import sys

import pyperclip

AMAZON = 'amazon'
CODE = 'pyb0f-20'
LINK = 'http://www.amazon.com/dp/{}/?tag={}'
# https://pybit.es/mastering-regex.html
URL = re.compile(r"""
    ^https://(?:www.)?amazon.[^/]+?/
    [^/]+/
    dp/
    (?P<asin>[^/]+)  # the numberic asin follows the dp/
    /ref=.*""", re.VERBOSE)

# https://pybit.es/pyperclip.html
url = pyperclip.paste()

if AMAZON not in url or '/dp/' not in url:
    sys.exit('Copy URL and run this script again')

print('Grabbed link from clipboard: \n'.format(url))

m = URL.match(url)
if not m:
    sys.exit('URL does not match')

asin = m.group('asin')
link = LINK.format(asin, CODE)

pyperclip.copy(link)
print('Copied link to clipboard: \n{}'.format(link))
