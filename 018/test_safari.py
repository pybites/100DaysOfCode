from datetime import datetime
import xml

import safari
from safari import get_rss_feed, get_tweets, gen_hashtags
from titles import test_titles

# monkey patch NOW in safari.py to work with fixed dt
# or use fixture? (TODO)
safari.NOW = datetime(2017, 4, 14, 16, 23, 00)

filters = 'python security haskell web'.split()
# http://stackoverflow.com/questions/38194403/list-to-dictionary-even-items-as-keys-odd-items-as-values
titles = dict(zip(test_titles[::2], test_titles[1::2]))


def test_get_rss_feed():
    doc = get_rss_feed()
    assert isinstance(doc, xml.etree.ElementTree.ElementTree)


def test_get_tweets_filters():
    tweets = list(get_tweets(greps=filters, goback_days=2))
    assert len(tweets) == 7  # tests timedelta
    assert not any('Microsoft Dynamics NAV' in tw for tw in tweets)
    assert all(tw in titles.values() for tw in tweets)
    filters_upper = list(map(str.upper, filters))
    tweets = list(get_tweets(greps=filters_upper, goback_days=2))
    assert len(tweets) == 7  # should not matter


def test_get_tweets_all_titles():
    tweets = list(get_tweets(greps=list('aeiou'), goback_days=10))
    assert len(tweets) == 100
    assert any('Microsoft Dynamics NAV' in tw for tw in tweets)


def test_get_tweets_no_titles():
    tweets = list(get_tweets(greps=['python'], goback_days=1))
    assert len(tweets) == 0


def test_gen_hashtags():
    for title, expected_hashtag in titles.items():
        hashtag = ' '.join(gen_hashtags(title, filters))
        if title != hashtag:
            assert hashtag not in title
        assert hashtag in expected_hashtag
