'''fun exercise in OOP and dunder methods'''

MAX_POINTS = 3


class Employee:
    '''Employee base class'''
    count = 0  # class var to keep track of how many people are around

    def __init__(self, name):
        self.name = name
        self.karma = 0
        Employee.count += 1
        self.klout = 1

    def _validation(self, points):
        limit = MAX_POINTS * self.klout
        if not isinstance(points, int) or abs(points) > limit:
            raise ValueError('need int points of <= {}'.format(limit))

    def __lshift__(self, points):
        points = self.klout * points
        self._validation(points)
        self.karma += points

    def __rshift__(self, points):
        points = self.klout * points
        self._validation(points)
        self.karma -= points

    def __str__(self):
        role = self.__class__.__name__
        return '{} ({} = klout: {}) has {} karma'.format(
            self.name, role, self.klout, self.karma)


class Manager(Employee):
    '''Manager and subsequent subclasses have more klout.
       This leads them to get more points (yeah it sucks)'''

    def __init__(self, name):
        super().__init__(name)
        self.klout = 2


class Director(Employee):
    '''He will get a lot of points'''

    def __init__(self, name):
        super().__init__(name)
        self.klout = 3


class VicePresident(Employee):
    '''She will get be world famous lol'''

    def __init__(self, name):
        super().__init__(name)
        self.klout = 4


if __name__ == '__main__':
    m = Employee('pybites')
    m << 3
    try:
        m << 4
        raise Exception('should not get here, max is 3 points + or -')
    except:
        pass
    m >> 2
    try:
        m >> 5
        raise Exception('should not get here, max is 3 points + or -')
    except:
        pass
    m >> 1
    assert m.karma == 0
    m << 2
    m << 3
    assert m.karma == 5

    print()
    print('ok look at how unfair this script is ;)')
    print('with same points assigned to each roles:')
    print()

    a, b = Employee('bob'), Manager('julian')
    c, d = Director('tom'), VicePresident('tim')
    a << 3; a << 2; a >> 1; a << 2
    b << 3; b << 2; b >> 1; b << 2
    c << 3; c << 2; c >> 1; c << 2
    d << 3; d << 2; d >> 1; d << 2
    print('\n'.join([str(p) for p in [a, b, c, d]]))

    assert a.karma == 6
    assert b.karma == 12
    assert c.karma == 18
    assert d.karma == 24

    print()
    print('Community has {} members (cls var)'.format(Employee.count))
    print('1st Employee instance was for testing so was hidden')
