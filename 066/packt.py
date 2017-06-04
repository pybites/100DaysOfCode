'starting a script to login to packt and list ebooks and potentially download them'
import os
import pdb
from pprint import pprint as pp
import sys

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PACKT_EMAIL = os.environ.get('PACKT_USER') \
              or sys.exit('please set Packt user in env')
PACKT_PW = os.environ.get('PACKT_PW') \
           or sys.exit('please set Packt pw in env')
LOGIN_URL = 'https://www.packtpub.com/login'


class Packt:

    def __init__(self, email, pw):
        'setup'
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
        # Unable to locate element: My eBooks
        # so need some time for redirect to finish
        self._driver.implicitly_wait(3)

    def get_books(self):
        'go to ebooks tab and collect all data'
        self._driver.find_element_by_link_text('My eBooks').click()
        elems = self._driver.find_elements_by_class_name("product-line")
        return {e.get_attribute('nid'): e.get_attribute('title')
                for e in elems}

    def parse_html(self):
        'use BeautifulSoup'
        s = soup(self._driver.page_source, 'html.parser')
        elems = s.find_all(attrs={'class': 'product-line'})
        pdb.set_trace()
        return elems


def main():
    p = Packt(PACKT_EMAIL, PACKT_PW)
    books = p.get_books()
    pp(books)
    # TODO: use other parsers
    # p.parse_html()


if __name__ == '__main__':
    main()
