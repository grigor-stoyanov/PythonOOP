from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name=name, portion=portion, price=2.50, brand=brand)
