class Person:
    def __init__(self, name, surname):
        self.surname = surname
        self.name = name

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name, people):
        self.people = people
        self.name = name

    # @property
    # def people(self):
    #     return self._people
    #
    # @people.setter
    # def people(self, value):
    #     if not value:
    #         value = []
    #     self._people = value

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f'{self.name} {other.name}', self.people + other.people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([ele.__repr__() for ele in self.people])}'

    def __getitem__(self, item):
        return f'Person {item}: {repr(self.people[item])}'

    # def __iter__(self):
    #     return iter([f'Person {i}: {ele}' for i, ele in enumerate(self.people)])


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(third_group)
print(len(first_group))
print(second_group)
# print(third_group[0])
for person in third_group:
    print(person)
