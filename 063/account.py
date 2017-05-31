from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'date amount')


class Account:

    def __init__(self, owner, start_balance=0):
        self.owner = owner.title()
        self.start_balance = start_balance
        self._transactions = []

    # first property use case: computed attributes

    @property
    def balance(self):
        tt = sum(t.amount for t in self._transactions)
        return self._start_balance + tt

    # second property use case: encapsulation

    @property
    def start_balance(self):
        return self._start_balance

    @start_balance.setter
    def start_balance(self, balance):
        if not isinstance(balance, int):
            raise TypeError('Start balance needs to be int')
        if balance < 0:
            raise ValueError('Start balance cannot be negative')
        self._start_balance = balance

    @start_balance.deleter
    def start_balance(self):
        raise AttributeError('Cannot delete start_balance attr')

    # (not property related)
    # transaction management with magic methods

    def _add_transaction(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Amount needs to be of type int')
        t = Transaction(datetime.now(), amount)
        self._transactions.append(t)

    def __iadd__(self, amount):
        'Magic method to allow for acc += amount'
        self._add_transaction(amount)
        return self  # need to return object!

    def __isub__(self, amount):
        'Magic method to allow for acc -= amount'
        self._add_transaction(-amount)
        return self

    def __len__(self):
        'len(acc_instance) gives # transactions'
        return len(self._transactions)

    def __str__(self):
        'Nice class reporting when doing str(acc_instance)'
        tt = ['- {}'.format(t) for t in self._transactions]
        s = ['Account of {}:'.format(self.owner),
             'Start Balance: {}'.format(self.start_balance),
             'Transactions:',
             '\n'.join(tt) or 'None',
             'End Balance: {}'.format(self.balance)]
        return '\n\n'.join(s)


if __name__ == '__main__':
    acc = Account('Bob', 100)
    acc += 25
    acc -= 100
    acc += 50
    acc -= 10
    print(acc)
