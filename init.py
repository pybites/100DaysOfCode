import datetime
import os

LOG = 'LOG.md'
DAY_ZERO = datetime.datetime(2017, 3, 29)  # = PyBites 100 days :)
NUM_DAYS = 100
NUM_WIDTH = 3
TABLE_HEADER = '''## Progress Log

| Day | Date | Created | Learned |
| --- | --- | --- | --- |
'''
DAY = '| {0} | {1} | [TITLE]({0}) | LEARNING |\n'
INIT_FILE = '__init__.py'
AUTHOR = "__author__ = 'PyBites'\n"


def gen_days():
    '''Generate day range 001...100'''
    for day in range(1, NUM_DAYS + 1):
        yield str(day).zfill(NUM_WIDTH)


def get_date(day):
    '''Get date by offsetting nth day from day 0'''
    date = DAY_ZERO + datetime.timedelta(int(day))
    return date.strftime('%b %d, %Y')


def create_log():
    '''Create progress log file with markdown table '''
    with open(LOG, 'w') as f:
        f.write(TABLE_HEADER)
        for d in gen_days():
            date = get_date(d)
            f.write(DAY.format(d, date))


def create_init(path):
    '''Create init file so each day dir is package,
    and gets committed to git from the start'''
    initfile = os.path.join(path, INIT_FILE)
    with open(initfile, 'w') as f:
        f.write(AUTHOR)


if __name__ == '__main__':
    if os.path.isfile(LOG):
        print('Logfile already created')
    else:
        print('Creating logfile')
        create_log()

    dirs = [d for d in gen_days() if not os.path.isdir(d)]
    if not dirs:
        print('All 100 days directories already created')
    else:
        print('Creating missing day directories')
        for d in dirs:
            os.makedirs(d)
            create_init(d)
