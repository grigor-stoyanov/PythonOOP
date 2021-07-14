# encapsulation the 2nd pillar of oop
# packing of data into a single component
# restricting access to prevent accidental modification
# python doesn't have modifiers like public,private,protected like in java
# everything within the class is public by default
# and access is modified trough syntax with _ or __
class BankAccount:
    def __init__(self, name):
        self.name = name
        # convention that hides the card number
        # __ private are not seen within the class or its children
        # called mangling it hides the variable in _BankAccount__card_num
        self.__card_num = 123456790
        # protected attributes with _ does nothing but specify
        # the attribute should not be modified outside the class
        self._exp_date = '24-Jul-2024'
        self.cvv = 599


class ExtendedBankAccount(BankAccount):
    def __init__(self, name, discount):
        super().__init__(name)
        # __ hides attribute within inheritance too
        # print(self.__card_num)
        print(self._exp_date)
        self.discount = discount


my_account = BankAccount('Pesho')
# mangled name of private attribute
print(my_account._BankAccount__card_num)
# setting a new private attribute is interpreted as adding a new attribute dynamically to the class
my_account.__card_num = 'Error'
my_account2 = ExtendedBankAccount('Gosho', 5)


# getter and setter are used to change the variables and access them within the class
class User:
    def __init__(self, name, is_admin):
        self.is_admin = is_admin
        self.name = name


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def info(self, user):
        return self.get_age(user)

    def get_age(self, user):
        if user.is_admin:
            return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError('Invalid Age')
        self.__age = age


# this allows us to modify attributes under certain conditions
# by placing them in methods within their class
super_admin = User('Admin', True)
person = Person('Ines', 30)
print(person.info(super_admin))
person.set_age(19)
print(person.get_age(super_admin))


# pythonic way of making getter and setter is using decorators
class Person2:
    def __init__(self, name, age=0):
        self.name = name
        # making attribute private will not call setter on initialisation
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    # everytime age is assigned a value(anywhere in the code) it goes trough this code
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than 0")
        # must be private to avoid recursion!
        # python things variable is the same name as the method
        self.__age = value

    def __getattr__(self, name):
        return 'Hello'

    def __setattr__(self, key, value):
        self.__dict__[key] = value.upper()


p = Person2('Ines', 30)

# methods can also be privated and mangled to be accessed within the class
# see Email Validator

# getattr(obj,attr,default) is used to access the attribute of an object
print(getattr(p, 'age'))
# print(getattr(p, 'nonexist')) raise attribute error
print(getattr(p, 'height', 'No such attribute'))
# when we call person.name __getattr__(self) is called and can be rewritten
print(p.name)
print(p.age)
# hasattr(obj,attr) first checks if attribute exists and returns true/false
# setattr(obj,attr,value) set attribute and return none
# they all have their own dunder methods when assignment is called
# delattr() deletes attribute as if it was never inited
