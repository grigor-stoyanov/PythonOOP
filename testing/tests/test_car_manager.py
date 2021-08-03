from unittest import TestCase, main

from testing.CarManager.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car('bmw', 'x5', 5.5, 100)

    def test_init_car(self):
        self.assertEqual('bmw', self.car.make)
        self.assertEqual('x5', self.car.model)
        self.assertEqual(5.5, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_set_fuel_capacity(self):
        self.car.fuel_capacity = 20
        self.assertEqual(20, self.car.fuel_capacity)

    def test_empty_model_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_empty_make_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_negative_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_set_fuel_consumption(self):
        self.car.fuel_consumption = 20
        self.assertEqual(20, self.car.fuel_consumption)

    def test_refill_adds_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_negative_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as e:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))

    def test_drive_without_fuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as e:
            self.car.drive(100)
        self.assertEqual('You don\'t have enough fuel to drive!', str(e.exception))

    # def test_drive_negative_distance_raises(self):
    #     self.car.refuel(100)
    #     self.assertEqual(10,self.car.fuel_amount)
    #     with self.assertRaises(Exception) as e:
    #         self.car.drive(-10)
    #     self.assertEqual('You can\'t drive with negative distance!',str(e.exception))
    def test_drive(self):
        distance = 50
        fuel = 100
        self.car.refuel(fuel)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(distance)
        fuel_consumed = (distance/100) * self.car.fuel_consumption
        self.assertEqual(fuel - fuel_consumed, self.car.fuel_amount)


if __name__ == '__main__':
    main()
