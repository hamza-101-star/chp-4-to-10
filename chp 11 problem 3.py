# employee.py

import unittest
from employee import Employee

class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the annual salary. Default is $5,000."""
        self.annual_salary += amount


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create an employee for use in all test methods."""
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        """Test the default raise of $5,000."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)


if __name__ == '__main__':
    unittest.main()
