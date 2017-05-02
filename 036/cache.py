from collections import defaultdict
from datetime import datetime
import pickle
from random import choice

CACHE = 'data'
NAMES = ('bob', 'julian', 'martin', 'dante', 'snake')
TIMES = range(15, 61, 15)


def gen_random_entry():
    while True:
        yield datetime.now(), choice(NAMES), choice(TIMES)


class Cache:

    def __enter__(self):
        try:
            self.cache = pickle.load(open(CACHE, "rb"))
        except FileNotFoundError:
            self.cache = defaultdict(list)
        return self.cache

    def __exit__(self, exc_type, exc_val, exc_tb):
        pickle.dump(self.cache, open(CACHE, "wb"))


if __name__ == '__main__':
    it = gen_random_entry()

    with Cache() as wl:
        for i in range(5):
            d, n, t = next(it)
            wl[n].append((d, t))

    print('Cached work so far')
    print('(this will grow each time program is run)')
    print()
    col1, col2 = ('NAME', 'MINUTES')
    print('{:<10}: {}'.format(col1, col2))
    with Cache() as wl:
        for name, work in sorted(wl.items()):
            total = sum(w[1] for w in work)  # TODO: use namedtuple
            print('{:<10}: {}'.format(name, total))
