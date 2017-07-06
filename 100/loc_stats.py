import glob
import os

import matplotlib.pyplot as plt

PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PATH)
DAY_PATTERN = os.path.join(BASE_DIR, '[0-9][0-9][0-9]')
INIT_FILE = '__init__.py'


def _count_lines(script):
    with open(script) as f:
        return len(f.readlines())


def count_loc():
    for day in glob.glob(DAY_PATTERN):

        loc = sum(_count_lines(script) for script in
                  glob.glob(os.path.join(day, '*.py'))
                  if not script.endswith(INIT_FILE))

        yield loc


def make_plot(locs, title):
    plt.hist(locs)
    plt.title(title)
    plt.xlabel('LOC per day')
    plt.ylabel('Frequency')
    plt.show()


if __name__ == '__main__':
    locs = list(count_loc())
    total = sum(locs)

    total_rounded = '{}K'.format(round(total/1000))
    title = 'PyBites #100DaysOfCode: we wrote {} LOC!'.format(total_rounded)
    print(title)

    make_plot(locs, title)
