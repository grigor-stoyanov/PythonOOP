from project.animals.animal import Bird
from project.food import *


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 0.25
        self.acceptable_food = [Meat]

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    def make_sound(self):
        return 'Cluck'

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increment = 0.35
        self.acceptable_food = [Meat, Vegetable, Fruit, Seed]
