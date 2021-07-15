from project.dough import empty_string_pro, sub_zero_pro


class Pizza:
    def __init__(self, name: str, dough: object, toppings_capacity: int):
        self.name = name
        self.toppings_capacity = toppings_capacity
        self.dough = dough
        self.toppings = {}
        self.toppings_count = 0

    name = empty_string_pro('name')
    toppings_capacity = sub_zero_pro('topping\'s_capacity')

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    def add_topping(self, topping: object):
        self.toppings_count += 1
        if self.toppings_count > self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) + topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
