import datetime
import re
import sys

import requests

TODAY = datetime.datetime.now()
HASHTAG_START = '#100DaysOfCode'
HASHTAG_END = '#Python'
CHALLENGE_DAYS = 100
START = datetime.datetime(2017, 3, 29)  # = PyBites 100 days :)
REPO_URL = 'https://github.com/pybites/100DaysOfCode/tree/master/'
NEW_SCRIPT = re.compile(r'\[(?P<title>.*?)\]\((?P<day>\d+)\)')

LOG = 'https://raw.githubusercontent.com/pybites/100DaysOfCode/master/LOG.md'
HTML = requests.get(LOG).text.split('\n')


def get_day_progress(day=TODAY):
    day = day.strftime('%b %d, %Y')

    for line in HTML:
        if day in line:
            field = line.split('|')[3].strip()
            m = NEW_SCRIPT.match(field)
            return m.groupdict()
    return None


def create_tweet(m=None):
    if m is None:
        m = get_day_progress()

    title = m['title']
    day = m['day']
    url = REPO_URL + day

    fmt = '{} - Day {}: {} {} {}'
    return fmt.format(
        HASHTAG_START, day,
        title, url, HASHTAG_END
    )


def get_date(args):
    try:
        y, m, d = [int(a) for a in args]
    except ValueError:
        raise

    try:
        day = datetime.datetime(y, m, d)
    except ValueError:
        raise

    diff = (day - START).days
    if not 0 < diff <= CHALLENGE_DAYS:
        raise ValueError('day outside 100 day challenge date range')

    return day


if __name__ == '__main__':

    script = sys.argv.pop(0)
    args = sys.argv

    if len(args) == 1 and args[0] == '-h':
        print('Usage: {} year month day')
        print('- if no args defaults to today'.format(script))
        sys.exit(1)

    elif len(args) == 3:
        try:
            day = get_date(args)
        except ValueError as exc:
            print('Error: {}'.format(exc))
            sys.exit(1)

    else:
        day = TODAY

    m = get_day_progress(day)
    if not m:
        print('Something went wrong parsing LOG file')
        sys.exit(1)

    tweet = create_tweet(m)
    print(tweet)
