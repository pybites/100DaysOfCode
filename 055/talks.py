from collections import namedtuple
import os
import sqlite3
import sys

from bs4 import BeautifulSoup as soup

from db import conn_db, DB

BASE_URL = 'https://us.pycon.org'
TABLE = 'talks'

Talk = namedtuple('Talk', 'title speaker description url')


def get_soup(html='index.html'):
    return soup(open(html).read(), 'html.parser')


def parse_talks(s):
    for talk in s.find_all(attrs={'class': 'slot-talk'}):
        title = talk.a.text
        speaker = talk.find(attrs={'class': 'speaker'}).text.strip()
        description = talk.a.get('title').strip()
        url = BASE_URL + talk.a.get('href')
        yield Talk(title=title,
                   speaker=speaker,
                   description=description,
                   url=url)


def create_table():
    cols = ', '.join(Talk._fields)
    idx = 'id INTEGER PRIMARY KEY AUTOINCREMENT,'

    with conn_db() as c:
        try:
            c.execute('CREATE TABLE {} ({} {})'.format(
                TABLE, idx, cols))
        except sqlite3.OperationalError:
            print('Table already exists')


def store_talks(talks):
    cols = Talk._fields

    placeholders = ', '.join(['?'] * len(cols))

    with conn_db() as c:
        c.executemany('INSERT INTO {} ({}) VALUES ({})'.format(
            TABLE, ', '.join(cols), placeholders), talks)


if __name__ == '__main__':
    s = get_soup()
    talks = parse_talks(s)

    if os.path.isfile(DB):
        print('{} already exists'.format(DB))
        sys.exit(1)

    create_table()
    store_talks(talks)
