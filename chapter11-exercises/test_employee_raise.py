import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Jose', 'Lopez', 55000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 60000)

    def test_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 65000)


unittest.main()
