from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):
    def make_sound(self):
        return 'Squeak'

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 0.1
        self.acceptable_food = [Vegetable,Fruit]


class Dog(Mammal):

    def make_sound(self):
        return 'Woof!'

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 0.40
        self.acceptable_food = [Meat]


class Cat(Mammal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 0.30
        self.acceptable_food = [Meat,Vegetable]

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):

    def make_sound(self):
        return 'ROAR!!!'

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 1
        self.acceptable_food = [Meat]
