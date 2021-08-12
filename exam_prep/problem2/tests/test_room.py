import unittest

# from project.appliances.appliance import Appliance
# from project.people.child import Child
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Room('goshovi', 350, 2)

    def test_correct_init(self):
        self.assertEqual('goshovi', self.r.family_name)
        self.assertEqual(350, self.r.budget)
        self.assertEqual(2, self.r.members_count)
        self.assertEqual([], self.r.children)
        self.assertEqual(0, self.r.expenses)

    def test_expense_property(self):
        self.assertEqual(0, self.r.expenses)
        self.r.expenses = 50
        self.assertEqual(50, self.r.expenses)

    def test_expense_negative_value(self):
        self.assertEqual(0, self.r.expenses)
        with self.assertRaises(ValueError) as e:
            self.r.expenses = -50
        self.assertEqual("Expenses cannot be negative", str(e.exception))

    # def test_calculate_expenses(self):
    #     self.r.calculate_expenses([Appliance(10), Appliance(20)], [Child(10, 9, 8, 7)])
    #     self.assertEqual(1920, self.r.expenses)
    #
    # def test_calculate_expenses_negative_value(self):
    #     with self.assertRaises(ValueError) as e:
    #         self.r.calculate_expenses([Appliance(-10), Appliance(-20)], [Child(-10, -9, -8, -7)])
    #     self.assertEqual("Expenses cannot be negative", str(e.exception))


if __name__ == '__main__':
    unittest.main()
