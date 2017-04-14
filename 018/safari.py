from datetime import datetime, timedelta
import os
import socket
import ssl
import sys
from urllib.request import urlopen
import xml
from xml.etree.ElementTree import parse

GOBACK_DEFAULT_DAYS = 1
NOW = datetime.now()
RSS = 'https://www.safaribooksonline.com/feeds/recently-added.rss'
LOCAL = 'MacBook' in socket.gethostname()
TWEET = 'New on @safari: {} - {}'


def get_tweets(greps=['Python'], goback_days=GOBACK_DEFAULT_DAYS):

    doc = get_rss_feed()

    # Python cookbook 3rd ed
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')[:-6]
        dt = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
        link = item.findtext('link')
        category = item.findtext('category')

        if (NOW - dt) > timedelta(days=goback_days):
            continue

        if not any(g.lower() in title.lower()
                   or g.lower() in category.lower()
                   for g in greps):
            continue

        title = ' '.join(gen_hashtags(title, greps))
        yield TWEET.format(title, link)


def get_rss_feed():
    if LOCAL:
        with open('recently-added.rss') as f:
            return parse(f)
    else:
        # work around SSL: CERTIFICATE_VERIFY_FAILED
        context = ssl._create_unverified_context()
        u = urlopen(RSS, context=context)
        return parse(u)


def gen_hashtags(title, greps):
    for word in title.split():
        if any(g.lower() == word.lower() for g in greps):
            yield '#' + word
        else:
            yield word


if __name__ == '__main__':

    filters = 'python security haskell web'.split()
    for tweet in get_tweets(greps=filters, goback_days=2):
        print(tweet)
