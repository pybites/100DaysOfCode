from collections import Counter
from string import punctuation, whitespace
import sys


def most_common_str(s, n=None):
    words = s.lower().translate(str.maketrans('', '', punctuation)).split()
    return Counter(words).most_common(n)


def most_common_re(s, n=None):
    return Counter(re.findall(rf'[^{punctuation}{whitespace}]+',
                              s.lower())).most_common(n)


def most_common_iter(s, n=None):
    return Counter(''.join(c for c in w if c not in punctuation)
                   for w in s.lower().split()).most_common(n)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        file = 'harry.txt'

    with open(file) as f:
        common_words = most_common_str(f.read(), n=20)

    for word, count in common_words:
        print('{:<4} {}'.format(count, word))
