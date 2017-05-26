roles = dict(employee=1, manager=2, director=3, svp=4, ceo=5)
max_points = 3

class Member:
    count = 0  # class variable

    def __init__(self, name, role_id, karma=0):
        self.name = name
        self.role_id = role_id
        self.karma = karma
        Member.count += 1

    '''
    # these are cool but pretty obscure code like ---m and ++m
    def __pos__(self):
        self.karma += 1

    def __neg__(self):
        self.karma -= 1
    '''

    def _validation(self, points):
        if not isinstance(points, int) or abs(points) > max_points:
            raise ValueError('need int points of <= {}'.format(max_points))

    def __lshift__(self, points):
        self._validation(points)
        self.karma += points 

    def __rshift__(self, points):
        self._validation(points)
        self.karma -= points 
        
    def __str__(self):
        return '{} (role_id: {}) has {} karma'.format(
            self.name, self.role_id, self.karma)


if __name__ == '__main__':
    m = Member('bob', roles.get('employee'), 0)
    m << 3
    try:
        m << 4
    except:
        print('exception = good, should not give more than 3 points')
    m >> 2
    try:
        m >> 5
    except:
        print('exception = good, should not subtract more than 3 points')
    m >> 1
    m << 3
    assert m.karma == 3
    print(m)

    mm = Member('tim', roles.get('manager'), 5)
    mm << 2
    mm << 3
    assert mm.karma == 10
    print(mm)

    print()
    print('The community now has {} active members'.format(Member.count))
