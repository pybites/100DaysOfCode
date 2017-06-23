from collections import Counter
import csv
import os
import re
import sys

regex_handle = re.compile(r'(@[a-zA-Z0-9_]+)')
regex_hashtag = re.compile(r'(#\S+)')
get_source = re.compile(r'<a.*?>([^<]+).*').sub
top = 10
width = 30
fmt = '{:<20} {:>5}'
bot = 'pybites'

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


def print_header():
    title = 'Twitter Archive report'
    print('=' * width)
    print(title.upper())
    print('=' * width)
    print()


def print_results(title, counter):
    print(title + ':')
    print('-' * width)
    for key, count in counter.most_common(top):
        print(fmt.format(key, count))
    print()


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
        if bot in src:
            src += ' (our bot)'
        sources[src] += 1

    print_header()
    print_results(title='Whose tweets', counter=tweets)
    print_results(title='Most mentioned', counter=mentions)
    print_results(title='Most used hashtags', counter=hashtags)
    print_results(title='Most active months', counter=activity)
    print_results(title='Sources used', counter=sources)
