from datetime import datetime, timedelta
import os
import socket
import ssl
import sys
from urllib.request import urlopen
from xml.etree.ElementTree import parse

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root)

from common.twitter_config import tweet_status

GO_BACK = timedelta(days=1)
NOW = datetime.now()
RSS = 'https://www.safaribooksonline.com/feeds/recently-added.rss'
LOCAL = 'MacBook' in socket.gethostname()
TWEET = 'New on @safari: {} - {}'


def get_tweets(greps=['Python']):

    doc = get_rss_feed()

    # Python cookbook 3rd ed
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')[:-6]
        dt = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
        link = item.findtext('link')
        category = item.findtext('category')

        if (NOW - dt) > GO_BACK:
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

    for tweet in get_tweets():
        if LOCAL:
            print(tweet)
        else:
            tweet_status(tweet)
