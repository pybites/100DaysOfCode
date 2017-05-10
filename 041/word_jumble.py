#!python3
#word_jumble.py is a script to print out every POSSIBLE word combination using the word or letters provided. Eg, if a 5 letter word is provided, it will not only provide valid words of 5 character length, but also 2 - 4 letters long.

import itertools

DICTIONARY = 'dictionary.txt'

def load_dictionary():
    words = []
    for i in open(DICTIONARY).readlines():
        words.append(i.lower().strip())
    return words
	
def check_word(dictionary, word):
    valid_words = []
    permutations = []
    for i in range(2, len(word)):
        perms = list(itertools.permutations(word, i))
        for x in perms:
            permutations.append(''.join(x))

    for i in permutations:
        if i in dictionary:
            valid_words.append(i)
    return set(valid_words)
	
def print_words(words):
    for i in words:
        print(i)

if __name__ == "__main__":
    ALL_WORDS = load_dictionary()
    user_word = input('Please enter a word to check: ').lower()
    print_words(check_word(ALL_WORDS, user_word))
