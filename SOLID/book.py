from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str, pages: int):
        self.content = content
        # adding pages
        self.pages = pages

# Solving Liskoff
class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class Formatter(BaseFormatter):
    def format(self, book: Book) -> str:
         return book.content[:self.pages]


class MobileFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        # we want to return less characters for mobile vesion
        return book.content[:20]


class DesktopFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:100]


class Printer:
    # instead we place formatter as argument as a Dependancy Injection!
    def get_book(self, book: Book, formatter):
        # we're instantiating in the Printer
        # now we need to add a new instance for mobile formatter!
        # formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book


printer = Printer()
formatter = MobileFormatter()
print(printer.get_book(Book("Random book noises"), formatter))
