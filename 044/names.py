import csv
from itertools import islice
import os
from random import choice
import ssl
import sys
from urllib.request import urlretrieve

CSV_DEST = 'https://raw.githubusercontent.com/yorkshiretwist/WTester/master/WTester/Helpers/CSV_Database_of_First_Names.csv'
CSV_FILE = os.path.basename(CSV_DEST)

# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>
ssl._create_default_https_context = ssl._create_unverified_context

if not os.path.isfile(CSV_FILE):
    print('CSV file not here, downloading it')
    try:
        urlretrieve(CSV_DEST, CSV_FILE)
    except Exception as exc:
        print(exc)
        sys.exit(1)

with open(CSV_FILE) as f:
    # get unique names
    names = list(set(row[0] for row in csv.reader(f)))


def gen_names():
    names_copy = list(names) # make a copy to be able to run the generator > 1 time
    while names_copy:
        name = choice(names_copy)
        names_copy.remove(name)
        yield name


if __name__ == '__main__':

    # test if all names are given by the generator
    assert len(names) == len(list(gen_names()))

    # give me 10 names
    for name in islice(gen_names(), 10):
        print(name)
