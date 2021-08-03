import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    # allows us to use same object for tests
    def setUp(self) -> None:
        self.worker = Worker('test', 100, 10)

    # by convention it must be named test
    def test_person_init(self):
        # Arrange and act
        # worker = Worker('test', 100, 10)
        worker = self.worker
        # assert
        # assert flipped result expected: actual
        self.assertEqual('test', worker.name)
        self.assertEqual(100, worker.salary)
        # msg optional argument on special cases
        self.assertEqual(worker.energy, 10, msg='Energy should be equal to the energy or init')
        self.assertEqual(worker.money, 0)

    def test_energy_increased_after_rest(self):
        # arrange
        # worker = Worker('tests', 100, 10)
        worker = self.worker
        self.assertEqual(10, worker.energy)
        # act
        worker.rest()
        # assert
        self.assertEqual(11, worker.energy)

    def test_person_works_with_negative_energy(self):
        # arrange
        worker = Worker('test', 100, 0)
        # act
        # we raise exeption and end test
        # to avoid use context manager
        with self.assertRaises(Exception) as ex:
            worker.work()
        # assert
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        worker = Worker('test', 100, 50)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.money)
        self.assertEqual(49, worker.energy)

    def test_get_info(self):
        worker = Worker('test', 100, 10)
        result = worker.get_info()
        expected = 'test has saved 0 money.'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
