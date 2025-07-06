# test_math_utils.py
import unittest
from math_utils import add, subtract, divide, med

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_med(self):
        digits=[1,2,3,4,5]
        self.assertEqual(med(digits), 3.0)

if __name__ == '__main__':
    unittest.main()
