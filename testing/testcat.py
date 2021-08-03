import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Sharo')

    def test_cat_init(self):
        self.assertEqual(self.cat.name, 'Sharo')
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(self.cat.size, 0)

    def test_cat_size_increased(self):
        self.assertEqual(self.cat.size, 0)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_can_not_eat(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_can_not_sleep(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry.', str(ex.exception))

    def test_cat_not_sleepy(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
