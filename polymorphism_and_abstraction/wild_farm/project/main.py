# second zero test
import unittest
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

class WildFarmTests(unittest.TestCase):
    def test_second_zero(self):
        hen = Hen("Harry", 10, 10)
        veg = Vegetable(3)
        fruit = Fruit(5)
        meat = Meat(1)
        self.assertEqual(str(hen), "Hen [Harry, 10, 10, 0]")
        self.assertEqual(hen.make_sound(), "Cluck")
        hen.feed(veg)
        hen.feed(fruit)
        hen.feed(meat)
        self.assertEqual(str(hen), "Hen [Harry, 10, 13.15, 9]")

if __name__ == "__main__":
    unittest.main()