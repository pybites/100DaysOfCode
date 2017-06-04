'''script to connect to packt and show ebooks
not done - todo:
    - download menu have 1... numbers not book ids
    - it is pretty slow, speed up
    - it is not showing all books, maybe html hidden to selenium?
    - urllib.request.urlretrieve ssl error
'''
from collections import defaultdict
import os
import re
import ssl
import sys
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PACKT_EMAIL = os.environ.get('PACKT_USER') \
              or sys.exit('please set Packt user in env')
PACKT_PW = os.environ.get('PACKT_PW') \
           or sys.exit('please set Packt pw in env')
LOGIN_URL = 'https://www.packtpub.com/login'

# hack ssl errors
ssl._create_unverified_context()


class Packt:

    def __init__(self, email, pw):
        self._email = email
        self._pw = pw
        self._driver = self._get_driver()
        try:
            self._login()
        except Exception as exc:
            print('Problem logging in: ')
            raise

    def _get_driver(self):
        'safaribooks py webscraping 2nd ed 9781786462589/'
        try:
            return webdriver.PhantomJS()
        except Exception:
            return webdriver.Firefox()

    def _login(self):
        'login to site'
        self._driver.get(LOGIN_URL)
        self._driver.find_element_by_id('edit-name').send_keys(
            self._email)
        self._driver.find_element_by_id('edit-pass').send_keys(
            self._pw + Keys.RETURN)
        self._driver.implicitly_wait(10)  # need time to load page
        self._driver.find_element_by_link_text('My eBooks').click()
        # import pdb; pdb.set_trace()

    def get_links(self):
        'get all links to later get downloads by bookid from'
        links = defaultdict(list)
        hrefs = [l.get_attribute('href') for l in
                 self._driver.find_elements_by_xpath("//a[@href]")]
        for l in hrefs:
            idx = re.sub(r'.*/(\d+)/.*', r'\1', l)
            links[idx].append(l)
        return links

    def get_books(self):
        'go to ebooks tab and collect all data'
        elems = self._driver.find_elements_by_class_name("product-line")
        return {e.get_attribute('nid'): e.get_attribute('title')
                for e in elems}


def show_books(books):
    for idx, title in books.items():
        print('{:<10} - {}'.format(idx, title))
    print()


def show_links(links, idx):
    if not links.get(idx):
        print('no links found')
        return

    for i, url in enumerate(links[idx], 1):
        print('({}) {}'.format(i, url))
    print()


def main():
    p = Packt(PACKT_EMAIL, PACKT_PW)

    books = p.get_books()
    links = p.get_links()

    while 1:
        show_books(books)
        idx = input('pick a book id: ')

        if 'q' in idx.lower():
            print('bye')
            break

        if idx not in books:
            print('book not in collection, try again')
            continue

        while 1:
            show_links(links, idx)
            try:
                linkid = int(input('link to download: ')) - 1
                url = links[idx][linkid]
                print(url)
            except ValueError:
                print('please choose a number')
                continue
            except IndexError:
                print('please choose a valid number')
                continue

            try:
                urlretrieve(url)
            except Exception as exc:
                print('problem downloading book: ')
                print(exc)
                continue

    # use to drop into shell:
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
