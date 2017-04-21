from collections import Counter
from string import punctuation
import sys


def strip_punctuation(word):
    '''Remove punctuation from a word'''
    return "".join(c for c in word if c not in punctuation)


def get_words(text):
    '''Converts text into set of words without punctuation'''
    with open(text) as f:
        words = f.read().lower().split()
    words = [strip_punctuation(word) for word in words]
    # could remove stopwords but requires nltk.corpus
    return filter(None, words)


def get_most_common(words, n=None):
    '''Return n common words, if n is None, return all (also singles)'''
    return Counter(words).most_common(n)


if __name__ == "__main__":
    try:
        harry = sys.argv[1]
    except IndexError:
        harry = 'harry.txt'

    words = get_words(harry)
    common_words = get_most_common(words, n=20)

    for word, count in common_words:
        print('{:<4} {}'.format(count, word))
