class Product:
    def __init__(self, name, price):
        self.__price = price
        self.__name = name

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name




