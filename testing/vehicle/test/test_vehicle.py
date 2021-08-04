import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(30.3, 150.4)

    def test_correct_init(self):
        self.assertEqual(self.vehicle.fuel, 30.3)
        self.assertEqual(self.vehicle.horse_power, 150.4)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.capacity, 30.3)

    def test_drive_successful(self):
        self.assertEqual(self.vehicle.fuel, 30.3)
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 17.8)

    def test_drive_unsuccessful(self):
        self.assertEqual(self.vehicle.fuel, 30.3)
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(30)
        self.assertEqual('Not enough fuel', str(e.exception))

    def test_refuel_successful(self):
        self.assertEqual(self.vehicle.capacity, 30.3)
        self.assertEqual(self.vehicle.fuel, 30.3)
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 27.8)

    def test_refuel_unsuccessful(self):
        self.assertEqual(self.vehicle.capacity, 30.3)
        self.assertEqual(self.vehicle.fuel, 30.3)
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(30)
        self.assertEqual('Too much fuel', str(e.exception))

    def test_string_representation(self):
        self.assertEqual(
            "The vehicle has 150.4 " \
            "horse power with 30.3 fuel left and 1.25 fuel consumption",
            str(self.vehicle)
        )


if __name__ == '__main__':
    unittest.main()
