roles = dict(employee=1, manager=2, director=3, svp=4, ceo=5)

class Member:
    count = 0  # class variable

    def __init__(self, name, role_id, karma=0):
        self.name = name
        self.role_id = role_id
        self.karma = karma

    def add(self, points):
        self.karma += points

    def subtract(self, points):
        self.karma -= points

    def __str__(self):
        return '{} (role_id: {}) has {} karma'.format(
            self.name, self.role_id, self.karma)


if __name__ == '__main__':
    m = Member('bob', roles.get('employee'), 0)
    print(m)
    m.add(2)
    print(m)
    m.subtract(3)
    print(m)
