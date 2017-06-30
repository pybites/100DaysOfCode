from collections import Counter
import re

regex_handle = re.compile(r'(@[a-zA-Z0-9_]+)')
regex_hashtag = re.compile(r'(#\S+)')
get_source = re.compile(r'<a.*?>([^<]+).*').sub
bot = 'pybites'


def _get_tweet_type(row):
    if row['in_reply_to_status_id']:
        return 'Reply'
    if row['retweeted_status_id']:
        return 'RT'
    return 'Own'


def _get_source(row):
    src = get_source(r'\1', row['source'])
    if bot in src:
        src += ' (our bot)'
    return src


def _get_mentions_or_hashtags(row, regex):
    matches = regex.findall(row['text'])
    return [m.lower() for m in matches]


def calc_stats(data):
    ret = {
        'tweets': Counter(),
        'mentions': Counter(),
        'hashtags': Counter(),
        'activity': Counter(),
        'sources': Counter(),
    }

    for row in data:
        tweet_type = _get_tweet_type(row)
        ret['tweets'][tweet_type] += 1

        for match in _get_mentions_or_hashtags(row, regex_handle):
            ret['mentions'][match] += 1

        for match in _get_mentions_or_hashtags(row, regex_hashtag):
            ret['hashtags'][match] += 1

        month = row['timestamp'][:7]
        ret['activity'][month] += 1

        src = _get_source(row)
        ret['sources'][src] += 1

    return ret
