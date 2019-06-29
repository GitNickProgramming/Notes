import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Adam', 'Smith', 50000)
        self.emp_2 = Employee('Jane', 'Crawford', 60000)
    
    def tearDown(self):
        pass 

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Adam.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Crawford@email.com')

        self.emp_1.first = 'Peter'
        self.emp_2.first = 'Sally'

        self.assertEqual(self.emp_1.email, 'Peter.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Sally.Crawford@email.com')


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Adam Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Crawford')

        self.emp_1.first = 'Peter'
        self.emp_2.first = 'Sally'

        self.assertEqual(self.emp_1.fullname, 'Peter Smith')
        self.assertEqual(self.emp_2.fullname, 'Sally Crawford')


    def test_apply_raise(self):
        self.emp_1 = Employee('Adam', 'Smith', 50000)
        self.emp_2 = Employee('Jane', 'Crawford', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success!')

            mocked_get.return_value.ok = False 

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Crawford/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main() 