class Book:
    # dunder methods are called "magicaly" by something else eg. symbol
    # self is the name of the variable and is self-asigned
    def __init__(self, name, author, pages, private):
        # on the current row attach the values to the variable
        self.name = name
        self.author = author
        self.pages = pages
        # using __ to an atribute privates it for use only within the class
        self.__private = private


# the init is called by "()" creating an instance of the object
book = Book('MyBook', 'Me', 200, 'something private')
# equivalent book = book.__init__('MyBook','Me',200)
print(book.pages)
print(book.name)
print(book.author)
# print(book.private)
# a different object allocated in memory
my_book = Book('MyBook', 'Me', 200)
