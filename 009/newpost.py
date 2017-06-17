import datetime
from datetime import date
import os
import re
import sys

import requests

PYB_CONTENT_DIR = os.environ.get('PYB_CONTENT_DIR') or os.path.expanduser('~')
LOGGED_IN_USER = os.getlogin()
DEFAULT_HOURS = 2
DEFAULT_IMAGE, SPECIAL_IMAGE = 'pb-article.png', 'pb-special.png'
KNOWN_USERS = {
    'juliansequeira': 'Julian',
    'bbelderb': 'Bob',
}
POST_HEADER = '''Title: {title}
Date: {post_time}
Category: {category}
Tags: {tags}
Slug: {slug}
Authors: {author}
Summary: {summary}
cover: images/featured/{image}
status: draft

{summary}
'''
POST_END = '''

---

Keep Calm and Code in Python!

-- {author}'''
CELEBRATION_MSG = '''*** HAPPY PYBITES CELEBRATION ({occasion}) !! ***

Hey, maybe you want to write something special today?!

No worries about the theme, I take care of:
- adding '{prefix}' in the slug
- use our nice featured image (oh yeah!)
- overwrite the author to 'PyBites'
- pick 'Special' for the category

Isn't that just awesome dog?!
PyBites definitely loves to automate stuff :)
'''
PYB_START = date(year=2016, month=12, day=19)
SPECIAL_DAY_OFFSETS = (100, 365)
SPECIAL_POST_NUM = 100
SPECIAL_SLUG_PREFIX = 'special'
BASE_URL = 'https://pybit.es'
TAG_URL = '{}/tags.html'.format(BASE_URL)
AUTHORS_URL = '{}/authors.html'.format(BASE_URL)


def get_future_time(hours=DEFAULT_HOURS):
    now = datetime.datetime.now()
    hours_ahead = datetime.timedelta(hours=hours)
    return (now + hours_ahead).strftime('%Y-%m-%d %H:%M')


def get_cats_or_tags(page, urldir):
    category = re.compile(
        r'<a href="%s/%s/[^"]+">(\w+)</a>'
        % (BASE_URL, urldir))
    html = requests.get('{}/{}.html'.format(BASE_URL, page)).text
    return category.findall(html)


def today_is_special_day():
    num_posts = get_num_posts() + 1
    if num_posts % SPECIAL_POST_NUM == 0:
        return True, '{} posts'.format(num_posts)

    age = get_age()
    if any(map(lambda x: age % x == 0, SPECIAL_DAY_OFFSETS)):
        return True, '{} days'.format(age)

    return False, 'No celebration'


def get_age():
    today = date.today()
    return (today - PYB_START).days


def get_num_posts():
    posts = re.compile(
        r'<a href="%s/author/[^"]+">\w+</a>\s\((\d+)\)'
        % BASE_URL)
    html = requests.get(AUTHORS_URL).text
    return sum(int(num) for num in posts.findall(html))


def write_template(slug, content):
    new_post = os.path.join(PYB_CONTENT_DIR, '{}.md'.format(slug))
    print('Awesome! Saving new post template to {}'.format(new_post))

    with open(new_post, 'w') as f:
        f.write('\n'.join(content))


def main():
    print('Lets write a new article :)')
    print()

    special_day, occasion = today_is_special_day()

    if special_day:
        print(CELEBRATION_MSG.format(occasion=occasion,
                                     prefix=SPECIAL_SLUG_PREFIX))
        image = SPECIAL_IMAGE

        author = 'PyBites'

        category = 'Special'
    else:
        image = DEFAULT_IMAGE

        author = KNOWN_USERS.get(LOGGED_IN_USER)
        inp = input('Author [{}]: '.format(author))
        if not author and not inp:
            sys.exit('Please provide a author')
        if inp:
            author = inp.strip().title()

        categories = ', '.join(get_cats_or_tags('categories', 'category'))
        category = input('Select a category [used: {}]: '.format(categories))

    hours = input('Publish in hours from now [{}]: '.format(DEFAULT_HOURS))
    try:
        hours = int(hours)
    except ValueError:
        if hours:
            print('Not an int value, using default ({})'.format(DEFAULT_HOURS))
        else:
            print('No hours given, using default ({})'.format(DEFAULT_HOURS))
        hours = DEFAULT_HOURS
    post_time = get_future_time(hours)

    tags = input('Select tags (comma seperated) [used: {}]: '.format(TAG_URL))
    tags = ', '.join([tag.strip() for tag in tags.split(',')])

    summary = input('A compelling summary please (this shows up in Google!): ')
    title = input('A gripping title (make it awesome, ok?): ')
    title = title.replace(':', '')  # pelican does not like colons in title
    slug = input('And lastly make the slug (= filename) - SEO counts, ok? ')

    if special_day and SPECIAL_SLUG_PREFIX not in slug:
        print('No {} in slug, prepending it'.format(SPECIAL_SLUG_PREFIX))
        slug = '{}-{}'.format(SPECIAL_SLUG_PREFIX, slug)

    content = [POST_HEADER.format(title=title,
                                  post_time=post_time,
                                  category=category,
                                  tags=tags,
                                  slug=slug,
                                  author=author,
                                  summary=summary,
                                  image=image)]
    content += ['## header {}\n\n'.format(i) for i in range(1, 6)]
    content += [POST_END.format(author=author)]

    write_template(slug, content)


if __name__ == '__main__':
    main()
