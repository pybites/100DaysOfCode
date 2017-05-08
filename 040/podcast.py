from email.mime.text import MIMEText
import os
import random
import shelve
import smtplib
import sys
import time

import feedparser
import schedule

CACHE = 'cache'


class Episode:

    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link
        self.done = False

    def __str__(self):
        status = 'done' if self.done else 'not done'
        return 'Podcast {}: {} - {} (status: "{}")'.format(self.id, self.title, self.link, status)


def store_new_episodes(feed):
    episodes = _parse_feed(feed)
    _update_cache(episodes)


def _parse_feed(feed):
    for e in feedparser.parse(feed)['entries']:
        id, title, link = e.get('id'), e.get('title'), e.get('link')
        yield Episode(id, title, link)


def _update_cache(episodes):
    with shelve.open(CACHE) as s:
        for ep in episodes:
            if ep.id not in s:
                s[ep.id] = ep


def get_random_episode():
    with shelve.open(CACHE) as s:
        episodes = list(s.keys())
        random.shuffle(episodes)
        for key in episodes:
            ep = s[key]
            if ep.done:
                print('Nope cannot take this episode as already listened ({})'.format(ep))
                continue
            print('Episode to listen to next: {}'.format(ep))
            ep.done = True
            s[key] = ep
            return ep
        else:
            print('No unplayed episodes, stay tuned')


def mail_episode(ep):
    # ok did cheat here, got this from cverna
    # https://github.com/pybites/challenges/blob/community/17/cverna/podcast.py
    # TODO: test on server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_account = os.environ.get('MAIL_ACCOUNT') or sys.exit('Need mail user')
    smtp_password = os.environ.get('MAIL_PASSWORD') or sys.exit('Need mail pw')
    mailto = os.environ.get('MAILTO') or sys.exit('Need mail to')
    smtp_server.ehlo()
    smtp_server.starttls()
    try:
        smtp_server.login(smtp_account, smtp_password)
    except smtplib.SMTPAuthenticationError:
        print('Could not login to the smtp server please check your username and password')
        sys.exit(1)
    msg = MIMEText('\nHi this week podcast is {} you can download it from here {}'.
                   format(ep.title, ep.link))
    msg['Subject'] = 'My podcast of the week'
    msg['From'] = smtp_account
    msg['To'] = mailto
    smtp_server.send_message(msg)
    smtp_server.quit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Specify a feed rss feed please')
        sys.exit(1)

    feed = sys.argv[1]

    schedule.every().tuesday.at("9:00").do(store_new_episodes, feed)
    schedule.every().wednesday.at("10:52").do(get_random_episode)

    while True:
        schedule.run_pending()
        time.sleep(1)
