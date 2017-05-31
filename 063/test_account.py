import pytest

from account import Account

acc = Account('bob', 10)


def test_wrong_type():
    with pytest.raises(TypeError):
        Account('bob', 'spam')
    with pytest.raises(ValueError):
        Account('bob', -10)
    assert acc.start_balance == 10


def test_deleter():
    with pytest.raises(AttributeError):
        del acc.start_balance


def test_can_still_set_int_attr():
    acc._start_balance = 100
    assert acc.start_balance == 100


def test_balance():
    acc2 = Account('Tim', 100)
    assert acc2.start_balance == 100
    acc2 += 25
    acc2 -= 100
    acc2 += 50
    acc2 -= 10
    assert acc2.balance == 65
    assert len(acc2) == 4


def test_type_checking_on_isub_iadd():
    acc2 = Account('Tim', 100)
    with pytest.raises(TypeError):
        acc2 += 'foo'
    with pytest.raises(TypeError):
        acc2 -= 'bar'


if __name__ == '__main__':
    pytest.main()
