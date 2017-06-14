# -*- coding: utf-8 -*-
from collections import defaultdict, namedtuple
import os
import re
import sys

from bs4 import BeautifulSoup as Soup
import requests


PACKT_EMAIL = os.environ.get('PACKT_USER')
PACKT_PW = os.environ.get('PACKT_PW')
if not PACKT_EMAIL or not PACKT_PW:
    sys.exit('please set Packt user and password in env')

BASE_URL = 'https://www.packtpub.com'
LOGIN_URL = BASE_URL + '/register'
EBOOKS_URL = BASE_URL + '/account/my-ebooks'

HEADERS = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'  # noqa E501
                         '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}  # noqa E501

DEST_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'books', 'Packt')
FMT = '{:>3}) {}'
BOOK_FORMATS = ('pdf', 'epub', 'mobi')

Book = namedtuple('Book', 'nid title')
session = requests.Session()


def check_dir(folder):
    """Check to see if directory exists and create it if it doesn't"""
    if not os.path.exists(folder):
        os.makedirs(folder)


def login():
    form_data = {'email': PACKT_EMAIL,
                 'password': PACKT_PW,
                 'op': 'Login',
                 'form_build_id': '',
                 'form_id': 'packt_user_login_form'}
    session.post(LOGIN_URL, headers=HEADERS, data=form_data)


def get_acc_ebooks_html():
    return session.get(EBOOKS_URL, headers=HEADERS).text


def get_product_download_links(soup):
    books = defaultdict(list)
    prev = 0
    library = soup.findAll("a", href=re.compile(r'_download/'))
    for link in library:
        href = link.attrs.get('href')
        nid = re.sub(r'.*_download/(\d+)/.*', r'\1', href)
        if 'code' in nid:
            nid = prev
        prev = nid
        full_href = BASE_URL + href
        books[nid].append(full_href)
    return books


def extract_metadata_books(soup):
    products = soup.findAll("div", {"class": "product-line"})
    for prod in products:
        nid = prod.attrs.get('nid')
        title = prod.attrs.get('title')
        if nid and title:
            yield Book(nid=nid, title=title)


def _check_exit(inp):
    if inp == 'q':
        print('Bye')
        sys.exit(0)


def _show_books(book_matches):
    for idx, book in enumerate(book_matches, 1):
        print(FMT.format(idx, book.title))


def _is_code_zip(ext):
    return ext.lower() not in BOOK_FORMATS


def _create_out_file(book, url):
    title = book.title.lower().replace('ebook', '')
    fname = re.sub('[^.a-z]+', '-', title).strip('-')
    ext = url.split('/')[-1]
    ext = 'zip' if _is_code_zip(ext) else ext
    file_name = '{}.{}'.format(fname, ext)
    return os.path.join(DEST_DIR, file_name)


def download_book(url, book, chunk_size=2000):
    print('Downloading {}'.format(url))
    r = session.get(url, headers=HEADERS, stream=True)
    out_file = _create_out_file(book, url)
    print('Saving to {}'.format(out_file))
    with open(out_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


if __name__ == '__main__':
    print('Packt download manager'.upper())
    print()

    print('Logging in')
    login()

    print('Retrieving books')
    ebooks_html = get_acc_ebooks_html()

    soup = Soup(ebooks_html, 'html.parser')

    download_links = get_product_download_links(soup)
    books = list(extract_metadata_books(soup))

    check_dir(DEST_DIR)

    # First go: get it working
    #  TODO: refactor - "Flat is better than nested."

    while True:
        print()
        search = input('Seach for a book (q = exit): ').lower()
        _check_exit(search)

        book_matches = [b for b in books if search in b.title.lower()]
        if not book_matches:
            print('No matches, try again')
            continue

        _show_books(book_matches)

        while True:
            bookid = input('Choose book (n = new search, q = exit): ').lower()
            _check_exit(bookid)
            if bookid == 'n':
                break

            try:
                index = int(bookid) - 1
                book = book_matches[index]
            except (ValueError, IndexError):
                print('Wrong input, please try again')
                continue

            if not download_links.get(book.nid):
                print('No download links for book nid {}'.format(book.nid))
                break

            while True:
                links = download_links[book.nid]
                for idx, url in enumerate(links, 1):
                    print(FMT.format(idx, url))

                prompt = 'Choose url ids separated by commas (e.g. 1,3)\n'
                prompt += 'a = download all / c = choose new book / q = exit: '
                inp = input(prompt).lower()
                _check_exit(inp)

                if inp == 'c':
                    _show_books(book_matches)
                    break

                if inp == 'a':
                    download_urls = range(1, len(links)+1)
                else:
                    download_urls = [u.strip() for u in
                                     inp.split(',')]

                for url in download_urls:
                    try:
                        index = int(url) - 1
                        dl_url = links[index]
                    except (ValueError, IndexError):
                        print('Wrong input, please try again')
                        continue

                    try:
                        download_book(dl_url, book)
                    except Exception as exc:
                        print('Oops cannot download: ', exc)
                        continue

                if inp == 'a':
                    print('All books downloaded')
                    break
