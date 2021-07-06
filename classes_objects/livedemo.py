class Car:
    # class attributes are attributes outside of innit and available to all instance of a class
    name = 'BMW'
    age = 22
    # private variable usable only within thee object
    __private = 0

    # init is always created with new instance of object even without atributes
    # because every class inherits it from object class
    def __init__(self, engine):
        # every object uses . operator to refer to attributes or methods
        self.engine = engine

    def instance_method(self):
        print('This method available within the instance of the object')

    # retrievs string representation of class instance
    def __str__(self):
        return f"This is a vehicle with {self.engine}"

    # machine interpreted from console and for print
    # however python searches first for str then represent
    def __repr__(self):
        return 'asd'

    @staticmethod
    def class_method():
        print('this method is available to the class')


car1 = Car('v55')
car2 = Car('v56')
# changes attribute looking from the instance to the class
car2.name = 'mercedes'
# changes attribute for the class looking only within the scope of the class
Car.name = 'generic name'
# if the class attribute is refent type aka list it will point towards same place in memory
# that means that changes of them in 1 object will apply to the oother
# dunder methods are built-in and provide different functionality inside and outside the class
# creates key_value pairs out of objects
print(Car.__dict__)
print(car2)
# when objects point to the same memory they are treated like the same even if they have different values
car2 = car1
print(car2 is car1)
# __doc__ attribute provides documentation of object as string """ This class does .... """
print(dict.__doc__)