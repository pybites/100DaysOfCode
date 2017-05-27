'''
Fun exercise in OOP and dunder methods: 

Give and take away karma points to/from 
Employee, Manager, Director, VicePresident

Final Karma is points * klout which each 
higher rank (subclass of Employee) has more off.

The lshift and rshift special methods make the syntax
for giving / taking away karma pretty cool:

obj << 3 = give 3 points to obj karma
obj >> 3 = take 3 points of obj karma 

I was going to use
+obj -obj
++obj --obj

with pos/neg dunders but this might be too obscure.
'''

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
    '''She will be world famous lol'''

    def __init__(self, name):
        super().__init__(name)
        self.klout = 4


if __name__ == '__main__':
    e1 = Employee('pybites')
    e1 << 3
    try:
        e1 << 4
        raise Exception('should not get here, max is 3 points + or -')
    except:
        pass
    e1 >> 2
    try:
        e1 >> 5
        raise Exception('should not get here, max is 3 points + or -')
    except:
        pass
    e1 >> 1
    assert e1.karma == 0
    e1 << 2
    e1 << 3
    assert e1.karma == 5
    print(e1)

    print()
    print('ok look at how unfair this script is ;)')
    print('with same points assigned to each roles:')
    print()

    e2, m1 = Employee('bob'), Manager('julian')
    d1, v1 = Director('tom'), VicePresident('tim')
    e2 << 3; e2 << 2; e2 >> 1; e2 << 2
    m1 << 3; m1 << 2; m1 >> 1; m1 << 2
    d1 << 3; d1 << 2; d1 >> 1; d1 << 2
    v1 << 3; v1 << 2; v1 >> 1; v1 << 2
    print('\n'.join([str(p) for p in [e2, m1, d1, v1]]))

    assert e2.karma == 6
    assert m1.karma == 12
    assert d1.karma == 18
    assert v1.karma == 24

    print()
    print('Community has {} members (cls var)'.format(Employee.count))
