import argparse
from collections import namedtuple
from datetime import datetime
import ssl
import time

import feedparser
from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DEFAULT_FEED = 'https://talkpython.fm/episodes/rss'

Base = declarative_base()

Episode = namedtuple('Episode', 'id title link published')


class Podcast(Base):
    __tablename__ = 'podcasts'
    id = Column('id', String(), primary_key=True)
    title = Column('title', String(), index=True)
    link = Column('link', String())
    published = Column('published', DateTime())
    done = Column('done', Boolean(), default=False)
    created_on = Column('created_on', DateTime(),
                        default=datetime.now)
    updated_on = Column('updated_on', DateTime(),
                        default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<Podcast(id='%s', title='%s', link='%s', \
                 published='%s', done='%s')>" \
               % (self.id, self.title, self.link, self.published, self.done)


engine = create_engine('sqlite:///podcast.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# some feeds get 'bozo_exception': URLError(SSLError(1,
#   '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context


def dump_episodes_to_db(episodes):
    records = [Podcast(id=ep.id, title=ep.title,
               link=ep.link, published=ep.published)
               for ep in episodes.values()]
    session.add_all(records)
    session.commit()


def parse_feed(feed):
    output = feedparser.parse(feed)

    d = {}
    for e in output['entries']:
        id = e.get('id')
        title = e.get('title')
        link = e.get('link')
        published = _to_dt(e.get('published_parsed'))
        d[id] = Episode(id, title, link, published)
    return d


def _to_dt(struct):
    return datetime.fromtimestamp(time.mktime(struct))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--feed', help='Podcast feed to parse')
    args = parser.parse_args()

    if args.feed:
        feed = args.feed
    else:
        feed = DEFAULT_FEED

    episodes = parse_feed(feed)
    dump_episodes_to_db(episodes)
