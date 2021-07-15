# static methods have no relation to the class
# it cannot modify an object or class state
class Person:
    def __init__(self, name):
        self.name = name

    # its first positional argument is not self
    @staticmethod
    def is_adult(age):
        return age >= 18
    # it helps for accidental modifications of the class
    # no dependency for unit test


# class methods are used to create factory methods
# they are shared between all instances and changing them must be cautious
class Pissa:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # factory pattern raising instance from the class
    @classmethod
    def peperoni(cls):
        return cls(['tomatosauce', 'parmesan', 'peperoni'])

    @classmethod
    def quatro_formagi(cls):
        return cls(['mocarela', 'gorgonsola', 'cheddar', 'parmigiano'])


# ensure correct instance creation and follows the DRY principle
first_p = Pissa.peperoni()


class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or \
                value > Person.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age
# rewriting/overriding method in the child class to keep the logic is necessary
    # if it is not defined it will use the parent method to validate
    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or \
                value > Employee.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
