from collections import Counter
import csv
import os
from pprint import pprint as pp
import re
import sys

regex_handle = re.compile(r'(@[a-zA-Z0-9_]+)')
regex_hashtag = re.compile(r'(#\S+)')
get_source = re.compile(r'<a.*?>([^<]+).*').sub
top = 10

tweets = Counter()
mentions = Counter()
hashtags = Counter()
activity = Counter()
sources = Counter()


def csv2dict(archive='tweets.csv'):
    if not os.path.isfile(archive):
        print('Please download archive and put in same folder as this script')
        sys.exit(1)

    with open(archive, 'r') as csvfile:
        for row in csv.DictReader(csvfile):
            yield row


if __name__ == '__main__':
    data = csv2dict()

    for row in data:
        if row['in_reply_to_status_id']:
            tweet_type = 'Reply'
        elif row['retweeted_status_id']:
            tweet_type = 'RT'
        else:
            tweet_type = 'Own'
        tweets[tweet_type] += 1

        matching_handles = regex_handle.findall(row['text'])
        if matching_handles:
            for handle in matching_handles:
                mentions[handle.lower()] += 1

        matching_hashtags = regex_hashtag.findall(row['text'])
        if matching_hashtags:
            for hashtag in matching_hashtags:
                hashtags[hashtag.lower()] += 1

        month = row['timestamp'][:7]
        activity[month] += 1

        src = get_source(r'\1', row['source'])
        sources[src] += 1

    title = 'Twitter Archive report'
    print(title.upper())
    print(len(title) * '-')
    print()

    print('Whose tweets?')
    pp(tweets.most_common(top))
    print()

    print('Most mentioned: ')
    pp(mentions.most_common(top))
    print()

    print('Most used hashtags: ')
    pp(hashtags.most_common(top))
    print()

    print('Most active months: ')
    pp(activity.most_common(top))
    print()

    print('Sources used: ')
    pp(sources.most_common(top))
    print()
