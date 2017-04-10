import os
import sys
import time

import feedparser

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root)

from common.twitter_config import tweet_status

DEFAULT_GOBACK_HOURS = 24
NOW = time.localtime()
RSS = 'http://feeds.feedburner.com/lyndacom-new-releases'
SEC_IN_HOUR = 60 * 60
TWEET = 'New @lynda course: {} - {}'


def get_tweets(grep):
    data = feedparser.parse(RSS)
    for item in data['entries']:
        url = item['id']
        title = item['title']
        published = item['published_parsed']

        diff = abs(time.mktime(published) - time.mktime(NOW))
        diff_hours = int(diff / (SEC_IN_HOUR))

        if diff_hours > DEFAULT_GOBACK_HOURS:
            continue

        if grep.lower() not in title.lower():
            continue

        yield TWEET.format(title.replace(grep, '#'+grep), url)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: $ python {} <grep>'.format(sys.argv[0]))
        sys.exit(1)

    grep = sys.argv[1].title()

    for tweet in get_tweets(grep):
        tweet_status(tweet)
