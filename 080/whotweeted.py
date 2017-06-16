'''
Who am I talking to PyBites?!
Fair question: https://twitter.com/anthonypjshaw/status/875275923930480641
'''

from functools import wraps
import os
import pickle
import re
import sys

import tweepy

DATA = 'data'
KNOWN_PLACES = dict(AU='Julian', ES='Bob')
PYBITES = 'pybites'
COLLECT_TEST_DATA = False
TWITTER_KEY = os.environ.get('PYB_100D_TW_KEY')
TWITTER_SECRET = os.environ.get('PYB_100D_TW_SECRET')
if not TWITTER_KEY or not TWITTER_SECRET:
    print('Please set PYB_100D_TW_KEY and PYB_100D_TW_SECRET env vars')
    sys.exit(1)

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)


def cache(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        tweetid = args[0]
        cache = os.path.join(DATA, tweetid)
        r = f(*args, **kwargs)
        if COLLECT_TEST_DATA:
            pickle.dump(r, open(cache, "wb"))
        return r
    return wrapped


def load_cache(tweetid):
    cache = os.path.join(DATA, tweetid)
    return pickle.load(open(cache, "rb"))


@cache
def get_status(tweetid):
    return api.get_status(tweetid)


def get_country_code(tweetid):
    try:
        tweet = get_status(tweetid)
    # this could be various issues so print the exception string
    except tweepy.error.TweepError as exc:
        raise ValueError('Problem getting tweet:\n{}'.format(exc))

    if tweet.user.screen_name != PYBITES:
        raise ValueError('Not a {} tweet'.format(PYBITES))

    try:
        return tweet.place.country_code
    except AttributeError:
        raise


def who_is_output(country):
    if not country:
        return 'Unable to identify country code'

    if country not in KNOWN_PLACES:
        return 'WTF?! Tweet was tweeted from {}'.format(country)

    return '{} tweeted it out'.format(KNOWN_PLACES[country])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide tweet id or link')

    tweetid = re.sub(r'.*status/(\d+).*', r'\1', sys.argv[1])

    try:
        country_code = get_country_code(tweetid)
    except ValueError as exc:
        print(exc)
    except AttributeError as exc:
        print('Location not set on tweet')
    else:
        output = who_is_output(country_code)
        print(output)
