# first level of software testing are basic function testing - manual testing
# testing as a user for each change implemented
# not repeatable,hard,time consuming
# validating each unit of the software as designed - unit testing
# types of testing manual and automated (unit - testing parts of code (class init,saving data...ect)
# automated can be unit,integration,functional/UI/end2end(full flow test),system tests,regression tests...
# higher accuracy,reusable,increased coverage,bug detection,stability
# they exist on the pipelines of vcs's to ensure they work correctly before pushing
# unittest concept:
# fixture - a baseline testing environment to run all tests simultaneously
# test case - set of conditions tests to work each part of system
# test suite - collections of test cases
import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        # similar to if for tests
        # assert result == expected (if false raise error)
        self.assertEqual(result, expected_result)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def getfullname(self):
        return f'{self.first_name} {self.last_name}'

    def getage(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


class PersonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Luc', 'Lungren', 25)

    def test_getfullname(self):
        result = self.person.getfullname()
        expected_result = 'Luc Lungren'
        self.assertEqual(result, expected_result)

    def test_getage(self):
        result = self.person.getage()
        expecte_result = 'Luc Lungren is 25 years old'
        self.assertEqual(result, expecte_result)


# basic unittest terams
# assertEqual,assertTrue,assertIn,with assertRaises,SetUp(prepare fixture),unittest.main(provides cmd interface to test script)
if __name__ == '__main__':
    unittest.main()
# the advantage to unittests can be in an entirely different module
# mocking is a way to copy behaviour from outside services and classes used in class being tested
# a patch decorator is used to substitute given dependancy with our own input
# used to test payment provider or emails