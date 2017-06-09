from collections import defaultdict, namedtuple
import os
import re
import sys

from bs4 import BeautifulSoup as Soup
import requests


PACKT_EMAIL = os.environ.get('PACKT_USER') \
              or sys.exit('please set Packt user in env')
PACKT_PW = os.environ.get('PACKT_PW') \
           or sys.exit('please set Packt pw in env')

BASE_URL = 'https://www.packtpub.com'
LOGIN_URL = BASE_URL + '/register'
EBOOKS_URL = BASE_URL + '/account/my-ebooks'

HEADERS = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

DEST_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'books', 'Packt')

Book = namedtuple('Book', 'nid title')
session = requests.Session()


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
    for link in soup.findAll("a", href=re.compile(r'/ebook_download/')):
        href = link.attrs.get('href')
        nid = re.sub(r'.*ebook_download/(\d+)/.*', r'\1', href)
        full_href = BASE_URL + href
        books[nid].append(full_href)
    return books


def get_books(soup):
    products = soup.findAll("div", {"class": "product-line"})
    for prod in products:
        nid = prod.attrs.get('nid')
        title = prod.attrs.get('title')
        if nid and title:
            yield Book(nid=nid, title=title)


def download_book(url, book, chunk_size=2000):
    print('Downloading {}'.format(url))
    r = session.get(url, headers=HEADERS, stream=True)
    title = book.title.lower().replace('ebook', '')
    fname = re.sub('[^.a-z]+', '-', title).strip('-')
    ext = url.split('/')[-1]
    file_name = '{}.{}'.format(fname, ext)
    out_file = os.path.join(DEST_DIR, file_name)
    print('Saving to {}'.format(out_file))
    with open(out_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


if __name__ == '__main__':
    fmt = '{:>3}) {}'

    print('Logging in')
    login()

    print('Retrieving books')
    ebooks_html = get_acc_ebooks_html()

    soup = Soup(ebooks_html, 'html.parser')

    download_links = get_product_download_links(soup)
    books = list(get_books(soup))

    print()
    print('Packt download manager'.upper())

    # First go: get it working
    # TODO: refactor - "Flat is better than nested."

    while True:
        print()
        search = input('Seach for a book (q for exit): ').lower()
        if search == 'q':
            print('Bye')
            sys.exit(0)

        book_matches = [b for b in books if search in b.title.lower()]
        if not book_matches:
            print('No matches, try again')
            continue

        for idx, book in enumerate(book_matches, 1):
            print(fmt.format(idx, book.title))

        while True:
            bookid = input('Choose book (n for new search): ').lower()
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
                    print(fmt.format(idx, url))

                downloadid = input('Choose url (c to cancel): ').lower()
                if downloadid == 'c':
                    break

                try:
                    index = int(downloadid) - 1
                    dl_url = links[index]
                except (ValueError, IndexError):
                    print('Wrong input, please try again')
                    continue

                try:
                    download_book(dl_url, book)
                    break
                except Exception as exc:
                    print('Oops cannot download: ')
                    print(exc)
