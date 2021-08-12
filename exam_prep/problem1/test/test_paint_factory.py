import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.p = PaintFactory('test', 30)

    def test_correct_init(self):
        self.assertEqual('test', self.p.name)
        self.assertEqual(30, self.p.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.p.valid_ingredients)
        self.assertEqual({}, self.p.ingredients)

    def test_can_add_calculation_False(self):
        self.assertEqual(False, self.p.can_add(31))

    def test_can_add_calculation_True(self):
        self.assertEqual(True, self.p.can_add(30))

    def test_repr(self):
        result = f"Factory name: {self.p.name} with capacity {self.p.capacity}.\n"
        self.assertEqual(result, self.p.__repr__())

    def test_adding_not_valid_ingredient(self):
        with self.assertRaises(TypeError) as e:
            self.p.add_ingredient('tomato', 20)
        self.assertEqual(f'Ingredient of type tomato not allowed in PaintFactory', str(e.exception))

    def test_adding_ingredient_with_no_space(self):
        with self.assertRaises(ValueError) as e:
            self.p.add_ingredient('blue', 50)
        self.assertEqual("Not enough space in factory", str(e.exception))

    def test_adding_new_ingredient(self):
        self.p.add_ingredient('blue', 30)
        self.assertEqual({'blue': 30}, self.p.ingredients)

    def test_adding_existing_ingredient(self):
        self.p.ingredients = {'blue': 20}
        self.p.add_ingredient('blue', 5)
        self.assertEqual({'blue': 25}, self.p.ingredients)

    def test_remove_non_existing_ingredient(self):
        with self.assertRaises(KeyError) as e:
            self.p.remove_ingredient('blue', 20)
        self.assertEqual("'No such ingredient in the factory'", str(e.exception))

    def test_remove_too_much_of_ingredient(self):
        self.p.ingredients = {'blue': 20}
        with self.assertRaises(ValueError) as e:
            self.p.remove_ingredient('blue', 25)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(e.exception))

    def test_remove_ingredient(self):
        self.p.ingredients = {'blue': 20}
        self.p.remove_ingredient('blue', 20)
        self.assertEqual({'blue': 0}, self.p.ingredients)

    def test_product_property(self):
        self.assertEqual({}, self.p.products)


if __name__ == '__main__':
    unittest.main()
