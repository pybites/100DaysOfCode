from collections import namedtuple
from contextlib import closing
import codecs
import csv
import ssl
import sys
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

LOCAL_CSV = 'daily-python-tip.csv'  # for testing
REMOTE_CSV = 'https://t.co/oARrOmrin7'
FIELDS = 'time code name email admin1 admin2 published'.split()
CONTEXT = ssl._create_unverified_context()
TEST = False

Tip = namedtuple('Tip', 'time code name published')


def get_csv_entries():
    if TEST:
        action = open(LOCAL_CSV)
    else:
        action = closing(urlopen(REMOTE_CSV, context=CONTEXT))
    with action as f:
        if not TEST and sys.version_info.major > 2:
            f = codecs.iterdecode(f, 'utf-8')  # needed for urlopen and py3
        for entry in csv.DictReader(f, fieldnames=FIELDS):
            yield entry


def get_tips(terms):
    for d in get_csv_entries():
        tip = Tip(time=d['time'], code=d['code'],
                  name=d['name'], published=d['published'])
        matches = all([i.lower() in tip.code.lower() for i in terms])
        if matches:
            yield tip


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit('Call this script with one or more search terms')

    terms = sys.argv[1:]

    fmt = '{}.\n{} submitted a tip at {}:\n{}\n\n* Published: {}\n---\n\n'

    tips = list(get_tips(terms))

    if not tips:
        print('Nothing found, you can submit a tip here: bit.ly/pythontip')
    else:
        for num, tip in enumerate(tips, 1):
            pub = tip.published if bool(tip.published) else 'not yet'
            print(fmt.format(num, tip.name, tip.time, tip.code, pub))
