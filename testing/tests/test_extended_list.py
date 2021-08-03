from unittest import TestCase, main

from testing.List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3, 4, 5, 6)

    def test_init_creates_all_attributes(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], self.int_list._IntegerList__data)

    def test_init_takes_non_integers(self):
        list_intgers = IntegerList(1.2, 2.3, "3", "4")
        self.assertEqual([], list_intgers._IntegerList__data)

    def test_add_integer_is_added(self):
        result = self.int_list.add(100)
        self.assertEqual([1, 2, 3, 4, 5, 6, 100], result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add(5.5)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_remove_index_returns_elements(self):
        el = self.int_list.remove_index(3)
        self.assertEqual(4, el)
        self.assertEqual([1, 2, 3, 5, 6], self.int_list._IntegerList__data)

    def test_remove_index_not_in_range_raises(self):
        with self.assertRaises(IndexError) as e:
            self.int_list.remove_index(10)
        self.assertEqual('Index is out of range', str(e.exception))

    def test_get_with_valid_index_returns_element(self):
        el = self.int_list.get(0)
        self.assertEqual(1, el)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.int_list._IntegerList__data)

    def test_get_with_not_valid_index_raises(self):
        with self.assertRaises(IndexError) as e:
            self.int_list.get(10)
        self.assertEqual('Index is out of range', str(e.exception))

    def test_insert_adds_element_at_index(self):
        self.int_list.insert(0, 100)
        self.assertEqual([100, 1, 2, 3, 4, 5, 6], self.int_list._IntegerList__data)

    def test_insert_not_integer_raises(self):
        with self.assertRaises(ValueError) as e:
            self.int_list.insert(0, '100')
        self.assertEqual('Element is not Integer', str(e.exception))

    def test_insert_integer_to_non_valid_index_raises(self):
        with self.assertRaises(IndexError) as e:
            self.int_list.insert(100, 100)
        self.assertEqual('Index is out of range', str(e.exception))

    def test_get_biggest(self):
        result = self.int_list.get_biggest()
        self.assertEqual(6, result)

    def test_get_index(self):
        index = self.int_list.get_index(5)
        self.assertEqual(4, index)

    def test_get_index_with_invalid_num(self):
        index = self.int_list.get_index(100)


if __name__ == '__main__':
    main()
