import unittest

from project.pet_shop import PetShop


class PetShopTest(unittest.TestCase):
    def setUp(self) -> None:
        self.p = PetShop('test')

    def test_correct_init(self):
        self.assertEqual(self.p.name, 'test')
        self.assertEqual(self.p.food, {})
        self.assertEqual(self.p.pets, [])

    def test_add_food_raises(self):
        with self.assertRaises(ValueError) as e:
            self.p.add_food('asd', -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(e.exception))

    def test_add_new_food_success(self):
        self.assertEqual(self.p.add_food('asd', 5), f"Successfully added {self.p.food['asd']:.2f} grams of asd.")
        self.assertEqual(self.p.food, {'asd': 5.0})

    def test_add_existing_food_sucesss(self):
        self.p.food = {'asd': 5.0}
        self.assertEqual(self.p.add_food('asd', 5), f"Successfully added {5:.2f} grams of asd.")
        self.assertEqual({'asd': 10.0}, self.p.food)

    def test_add_pet_raises(self):
        self.p.pets = ['djaro']
        with self.assertRaises(Exception) as e:
            self.p.add_pet('djaro')
        self.assertEqual("Cannot add a pet with the same name", str(e.exception))

    def test_add_pet_success(self):
        self.assertEqual(f"Successfully added djaro.", self.p.add_pet('djaro'))
        self.assertEqual(self.p.pets,['djaro'])

    def test_feed_pet_raises(self):
        with self.assertRaises(Exception) as e:
            self.p.feed_pet('dopamine','djaro')
        self.assertEqual(f"Please insert a valid pet name",str(e.exception))
    def test_feed_pet_no_food(self):
        self.p.pets = ['djaro']
        self.assertEqual(self.p.feed_pet('dopamine','djaro'),f'You do not have dopamine')

    def test_feed_pet_less_than_100_food(self):
        self.p.pets = ['djaro']
        self.p.food = {'dopamine':99}
        self.assertEqual(self.p.feed_pet('dopamine','djaro'),"Adding food...")
        self.assertEqual(self.p.food,{'dopamine':1099.0})
    def test_feed_pet_enough_food(self):
        self.p.pets = ['djaro']
        self.p.food = {'asd': 100}
        self.assertEqual(self.p.feed_pet('asd','djaro'),'djaro was successfully fed')
    def test_repr(self):
        self.p.pets = ['djaro','baro','varo']
        self.assertEqual(self.p, 'Shop test:\nPets: djaro, baro, varo')
if __name__ == '__main__':
    unittest.main()
