# inheritance is one of the 4 pillars of OOP
# it allows for methods and attributes to be reusable from a certain parent class
# add features to classes without modifying them e.g. age validation
# transitive in nature
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        return 'Sleeping'

    def __repr__(self):
        return 'this is a person'


class Employee(Person):
    def __init__(self, name, age, id, date, job):
        # calls for the constructor of parent
        # super() returns temporary object of the superclass
        super().__init__(name, age)
        self.id = id
        self.date = date
        self.job = job

    def __repr__(self):
        return super().__repr__() + ' who is also an multiple_inheritence'


class Manager(Person):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type


bob = Employee('bob', 23, '234234', '23/02/2020', 'constructor')
print(bob)


# multiple inheritance when an object inherits data from 2 or more objects
class Mother:
    def __init__(self):
        self.mother_name = 'Maria'


class Father:
    def __init__(self):
        self.father_name = 'Adam'


class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name} Mother: {self.mother_name}'


# multilevel - When a child class becomes a parent class for another child class
class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):

    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address


# each child has more attributes than it's parents because it keeps calling super of its parent

# MRO order of which methods are inherited with multiple inheritence
# C3 linerisation algorithm from inside out
class Parent:
    pass


class FirstChild(Parent):
    pass


class SecondChild(Parent):
    pass


class GrandChild(SecondChild, FirstChild):
    pass


# mro of grandchild
print(GrandChild.mro())


# A mixin or interface is a class that is implementing a specific set of features that is needed in many different classes
# Mixins cannot be instantiated by themselves
# A mixin is a class which has no data, only methods
class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        pass


class Car(Vehicle):
    pass


class Clock():
    pass


class RadioMixin():
    def play_song_on_station(self, station_frequency):
        return f'playing song on radio frequency {station_frequency}'


class Car(Vehicle, RadioMixin):
    pass


class Clock(RadioMixin):
    pass
car = Car('Sofia')
clock = Clock()
print(car.play_song_on_station(95.0))
print(clock.play_song_on_station(100.3))