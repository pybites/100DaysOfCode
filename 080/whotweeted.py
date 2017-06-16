'''
Who am I talking to PyBites?!
Fair question: https://twitter.com/anthonypjshaw/status/875275923930480641
'''

import os
import re
import sys

import tweepy

KNOWN_PLACES = dict(AU='Julian', ES='Bob')
PYBITES = 'pybites'

TWITTER_KEY = os.environ.get('PYB_100D_TW_KEY')
TWITTER_SECRET = os.environ.get('PYB_100D_TW_SECRET')
if not TWITTER_KEY or not TWITTER_SECRET:
    print('Please set PYB_100D_TW_KEY and PYB_100D_TW_SECRET env vars')
    sys.exit(1)

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)


def get_country_code(tweetid):
    try:
        tweet = api.get_status(tweetid)
    except tweepy.error.TweepError:
        raise ValueError('Not a valid tweetid')

    if tweet.user.screen_name != PYBITES:
        raise ValueError('Not a {} tweet'.format(PYBITES))

    try:
        return tweet.place.country_code
    except AttributeError:
        raise


def who_is_output(country):
    if not country:
        print('Unable to identify country for tweet id')
        return

    if country not in KNOWN_PLACES:
        print('Tweet was tweeted from {}'.format(country), end=', ')
        print('is PyBites traveling or fooling the system?!')
        return

    print('{} tweeted out {}'.format(KNOWN_PLACES[country],
                                     tweetid))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide tweet id or link')

    tweetid = re.sub(r'.*status/(\d+).*', r'\1', sys.argv[1])

    try:
        country_code = get_country_code(tweetid)
    except ValueError as exc:
        print(exc)
    except AttributeError:
        print('Location not set on tweet')
    else:
        who_is_output(country_code)
