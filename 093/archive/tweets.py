import csv
import os
import sys

DEFAULT_ARCHIVE = 'tweets.csv'


def parse_csv(archive=DEFAULT_ARCHIVE):
    if not os.path.isfile(archive):
        print('Please download archive and put in same folder as this script')
        sys.exit(1)

    with open(archive, 'r') as csvfile:
        for row in csv.DictReader(csvfile):
            yield row
