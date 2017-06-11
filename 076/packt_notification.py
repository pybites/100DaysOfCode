from collections import namedtuple
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys

from bs4 import BeautifulSoup as Soup
import requests

FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_PACKT_EMAILS').split()

BASE_URL = 'https://www.packtpub.com'
FREE_LEARNING_PAGE = 'free-learning'
PACKT_FREE_LEARNING_LINK = BASE_URL + '/packt/offers/' + FREE_LEARNING_PAGE
TIME_LEFT = '{} hours and {} minutes'
SUBJECT = 'Free Packt ebook of the day: {} (time left: {})'

Book = namedtuple('Book', 'title description summary image link timeleft')


def retrieve_page_html():
    if os.path.isfile(FREE_LEARNING_PAGE):
        with open(FREE_LEARNING_PAGE) as f:
            return f.read()
    else:
        return requests.get(PACKT_FREE_LEARNING_LINK).text


def _create_time_left_string(countdown_unix_tstamp):
    expires = datetime.fromtimestamp(int(countdown_unix_tstamp))
    now = datetime.now()
    left = str(expires - now)
    hh, mm, _ = left.split(':')
    return TIME_LEFT.format(hh, mm)


def extract_book_data_page(content):
    soup = Soup(content, 'html.parser')
    book_image = soup.find('div', {'class': 'dotd-main-book-image'})
    link = BASE_URL + book_image.find('a').get('href')
    image = 'https:' + book_image.find('img').get('src')
    book_main = soup.find('div', {'class': 'dotd-main-book-summary'})
    title_div = book_main.find('div', {'class': 'dotd-title'})
    title = title_div.find('h2').text.strip()
    descr_div = title_div.find_next_sibling("div")
    description = descr_div.text.strip()
    summary_html = descr_div.find_next_sibling("div")
    js_countdown = book_main.find('span', {'class': 'packt-js-countdown'})
    countdown = js_countdown.get('data-countdown-to')
    timeleft = _create_time_left_string(countdown)
    return Book(title=title,
                description=description,
                summary=summary_html,
                image=image,
                link=link,
                timeleft=timeleft)


def generate_mail_msg(book):
    return '''<h2><a href='{link}'>{title}</a></h2>
        <div>{description}</div>
        <img src='{image}' title='{title}'>
        <hr>
        {summary_html}
        <h2><a href='{link}'>Download in {timeleft}</a></h2>'''.format(
                link=book.link,
                title=book.title,
                description=book.description,
                image=book.image,
                summary_html=book.summary,
                timeleft=book.timeleft)


def mail_html(subject, content, recipients=TO_MAIL):
    sender = FROM_MAIL
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    part = MIMEText(content, 'html')
    msg.attach(part)
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()


if __name__ == '__main__':
    if not FROM_MAIL or not TO_MAIL:
        print('Please set FROM_MAIL and TO_PACKT_EMAILS env vars')
        sys.exit(1)

    content = retrieve_page_html()
    book = extract_book_data_page(content)

    subject = SUBJECT.format(book.title, book.timeleft)
    msg_body = generate_mail_msg(book)

    mail_html(subject, msg_body)
