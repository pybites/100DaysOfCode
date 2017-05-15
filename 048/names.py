# awesome stuff!
# https://github.com/joke2k/faker
from itertools import islice

from faker import Factory

# cool can do Dutch names
fake = Factory.create('nl_NL')  # Julian: use en_AU

def gen_names():
    '''Compare this to gen_names of 044 :)'''
    while True:
        yield fake.name()


if __name__ == '__main__':
    print('Some random Dutch names: ')
    
    for name in islice(gen_names(), 10):
        print('\t' + name)

    print()
    print('To get a fixed set, use seed')
    print('fake.seed(4321)')
    fake.seed(4321)
    print()

    print('Some fixed set of Dutch names: ')
    for name in islice(gen_names(), 10):
        print('\t' + name)

