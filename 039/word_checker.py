#!python3
#word_checker.py is a script to print out every word combination using the word or letters provided.

import itertools

DICTIONARY = 'dictionary.txt'

def load_dictionary():
    words = []
    for i in open(DICTIONARY).readlines():
        words.append(i.lower().strip())
    return words
	
def check_word(dictionary, word):
    permutations = set(map(''.join, itertools.permutations(word)))
    return {w for w in permutations if w in dictionary}
	
def print_words(words):
    for i in words:
        print(i)

if __name__ == "__main__":
    ALL_WORDS = load_dictionary()
    user_word = input('Please enter a word to check: ').lower()
    print_words(check_word(ALL_WORDS, user_word))
