# SOLID principles
# single responsibility
# open/closed
# Liskov substitution
# interface segregation
# dependency inversion
# they are rules that make refactoring code easier
# extremely useful for high volume projects
# 1. Single Responsibility (SRP)
# each class should be responsible for only 1 thing and only 1 reason to change
# on web level we have different classes that get the info by the user,classes that manage it and
# send it to the servers, which send it to the database
from abc import abstractmethod, ABC


class Student:
    # sets attributes - manager
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name

    # 2nd responsibility logs into database - service
    # def register(self, student):
    #   pass
    def __str__(self):
        return f"id {self.id} and name {self.name}"


# we split it in 2 classes
class Register:
    def register(self, obj):
        with open('students.txt', 'w') as file:
            file.write(str(obj))

    def get(self, id):
        with open('students.txt', 'r') as file:
            for line in file.readlines():
                if id in line:
                    return line
        return None


registrator = Register()
student = Student(1, 'TEST')
registrator.register(student)


# 2.open for extension closed for modification (OCP)
# Abstraction,Mixin,Monkey-patching(pytests),Generic functions(overloading) is used to overcome it
class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.semester_tax = semester_tax
        self.average_grade = average_grade
        self.name = name

    @abstractmethod
    def get_discount(self):
        # if self.average_grade > 5:
        #   return self.semester_tax * 0.4
        # if we decide to extend the code we have to use elif
        # which modifies existing code rather than adding new one
        # elif self.average_grade > 4:
        #   return self.semester_tax * 0.2
        pass


# we don't modify existing methods and logic we just extend it to achieve more functionality
class FourtyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if self.average_grade > 5:
            return self.smester_tax * 0.4


class TwentyPercentDiscount(StudentTaxes):
    def get_discount(self):
        if 4 < self.average_grade < 5:
            return self.semester_tax * 0.2


discounter = FourtyPercentDiscount('TEST', 350, 5.50)
discounter = TwentyPercentDiscount('TEST', 350, 4.00)


# 3. Liskov substitution - Derived types must be substitutable with base type
# derived classes extend base class functionality without removing base behaviour
# Student is a substitute for Person? YES
# see duck.py
# LSP and polymorphism is connected because subclasses must have interchangable
# base methods that apply to every class "every duck can quack"
# children must be polymorphic with their parents
# Design smell: 1.Code checking type of class (solved with polymorphism),
# 2. overriden methods change behaviour (Caused by polymorphism,overarchitecture)
# adding methods from base class that are not used by children and
# must raise exception or change parent method behaviour
# 3. Base class must rely on sub classes (has no functionality)


# 4. Interface Segregation see entertainment-system.py
# A client shouldn't depend on methods it does not use
# this makes code very coupled(dependant) and hard to refactor
# Mixins are the workaround by providing multiple clients specific behaviour
# as long as they don't extend them unnecessarily
# python doesen't have interfaces instead we solve this issue by multiplying classes-mixins
class Shape(ABC):
    # Shape depends on its children! LSP Violation
    # if we add a triangle we have to add a new abstract method
    # and in base class are useless anyway
    # @abstractmethod
    # def draw_rectangle(self):
    #     pass
    #
    # @abstractmethod
    # def draw_circle(self):
    #     pass
    # unspecific shape - abstract
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    # def draw_rectangle(self):
    #     return 'Drawing..'
    def draw(self):
        return 'Drawing Rectangle!'
    # IRC violation! Rectangle doesen't know how to draw circle
    # def draw_circle(self):
    #     pass


# no more extra methods and Circle is substitutable with Shape
class Circle(Shape):
    def draw(self):
        return 'Drawing Circle'


class ThreeDModel(ABC):
    @abstractmethod
    def model_3d(self, shape):
        pass


# 5. Dependancy Inversion - See Book
# protecting code from volitile things
# eg. making an instance directly in the class
# dependancy injection for defining dependancies
class Student:
    def __init__(self, name, age, adress):
        self.age = age
        self.name = name
        # not every student has same adress!
        # address no init!
        # self.address = Address()
        self.address = address


class Adress:
    def __init__(self, city):
        pass


adress = Adress('London')
# we inject the ready instance in the student
# decreases coupling and doesen't require change in code behaviour
student = Student('test', 20, adress)
