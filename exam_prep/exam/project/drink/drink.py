from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self._price = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self._brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:0.2f}ml - {self.price:0.2f}lv"