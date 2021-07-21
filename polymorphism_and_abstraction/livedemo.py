# polymorphism and abstraction is the final pillar of oop
# ability to present same interface for differing underlying forms trough interface of base class
# a common interface(methods to be implemented) between classes
class Shape:
    def get_area(self):
        return None


# every triangle and circle are shapes
class Triangle(Shape):
    def __init__(self, a, ha):
        self.a = a
        self.ha = ha

    # overriding get_area method
    def get_area(self):
        return self.a * self.ha * 0.5


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r ** 2 * 3.14


class Square:
    def __init__(self, a):
        self.a = a

    def calculate_area(self):
        return 'Square method'


shapes = [Triangle(30, 6), Triangle(5, 8), Circle(3), Circle(10), Square(5)]
# polymorphism guarantees get_area method when a new shape is added
for shape in shapes:
    print(shape.get_area())


# without polymorphism a type check may be required to determine correct method call
# see robots
# Compile-time polymorphism doesen't exist in python
def calculate_area_of_square(number: float):
    return number * number


# in type oriented languages (compile type) an error occurs
a: int = 6
print(calculate_area_of_square(a))


# to overcome it they use method overloading for different types or arguments
# the last type method will override the earlier one in python
# there is no concept of overloading
def calculate_area_of_square(number: int):
    return number * number


print(calculate_area_of_square(a), end='', sep='...')


# overloading built-in methods
class Person(object):
    # old python syntax
    # every class inherits object which contains all the built-in dunder methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return max(self.age, other.age)


b = [1, 2, 3]
# list(1,2,3) class list inherits object and rewrites __repr__(): '[1,2,3]'
p = Person('Pesho', 20)
p1 = Person('Gosho', 23)
print(p)
# need to implement len interface
print(len(p))
print(p1 + p)
print(p.__add__(p1))


class ReversedInt:
    def __init__(self, value_int):
        self.value_int = value_int

    def __add__(self, other):
        return self.value_int - other


ri = ReversedInt(5)
print(ri + 5)
# unsupported operand 5(int).__add__(ri) the int class doesn't have custom __add__ logic
print(5 + ri)


# duck typing if it looks like a duck and quacks like a duck its a duck
# we dont care about type of object just but weather it has the method we need
class Cat:
    def sound(self):
        return 'meow'


class Train:
    def sound(self):
        return 'choo-choo'


for any_type in Cat(), Train():
    any_type.sound()

# see playing

# what is abstraction one of the 4 pillars
# reduces complexity hiding irrelevant data about objects
# in python it is used trough abc library and at least 1 abstract method
# abstract classes can only be inherited not instanced
# it requires children to implement/override his methods
from abc import ABC, abstractmethod


class Figure(ABC):
    # def __init__(self):
    #     if type(self) is Figure:
    #         raise Exception('An abstract class cannot be instantiated')
    @abstractmethod
    def area(self):
        pass
        # raise Exception('not implemented')

    def permieter(self):
        return Exception('not implemented')


# for the code to work area method must be implemented for rectangle
class Rectangle(Figure):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height


# it will throw errors until we implement the abstractmethod area
r = Rectangle(5, 6).area()
# ABC modules enforces particular methods and makes creating abstract classes easier
f = Figure()


# Abstraction
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # encapsulation
    @name.setter
    def name(self, value):
        if len(value < 3):
            raise ValueError('name must be 3 chars')
        self.__name = value

    # abstraction
    @abstractmethod
    def sound(self):
        pass


# inheritance(common valiators)
class Cow(Animal):
    def sound(self):
        return 'Moo'


class Dog(Animal):
    def dog(self):
        return 'Bao'


# polymorphism
for animal in Cow('betty'), Dog('sharo'):
    print(animal.sound())
