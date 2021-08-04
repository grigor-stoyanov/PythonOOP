import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Test', 'asd', 'foo')

    def test_mammal_innit_correct_attributes(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('asd', self.mammal.type)
        self.assertEqual('foo', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected = "Test makes foo"
        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        result = self.mammal.info()
        expected = "Test is of type asd"
        self.assertEqual(expected, result)

    def test_set_animal_attributes(self):
        self.mammal.name = 'test2'
        self.mammal.type = 'new'
        self.mammal.sound = 'bar'
        self.mammal._Mammal__kingdom = 'human'
        self.assertEqual('test2', self.mammal.name)
        self.assertEqual('new', self.mammal.type)
        self.assertEqual('bar', self.mammal.sound)
        self.assertEqual('human', self.mammal._Mammal__kingdom)


if __name__ == '__main__':
    unittest.main()
