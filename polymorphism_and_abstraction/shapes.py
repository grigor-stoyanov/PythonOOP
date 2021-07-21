from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return self.r ** 2 * 3.14

    def calculate_perimeter(self):
        return self.r * 2 * 3.14


class Rectangle(Shape):
    def __init__(self, h, w):
        self.w = w
        self.h = h

    def calculate_area(self):
        return self.w * self.h

    def calculate_perimeter(self):
        return self.w + self.h


s = Shape()
print(s)
