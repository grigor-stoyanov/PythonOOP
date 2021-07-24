class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0


class Reader:
    def turn_page(self, page):
        self.page = page
