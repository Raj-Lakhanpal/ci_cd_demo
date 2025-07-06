# test_math_utils.py
import unittest
from math_utils import add, subtract, divide, med, bill_after_discount

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
    
    def test_bill_after_discount(self):
        self.assertEqual(bill_after_discount(100, 10), 90)
    
    def test_full_logic_bill_after_discount(self):
        item_one = 12.99*3
        item_two = 4.50*2
        item_three = 1.25
        total_price = item_one+item_two+item_three
        final_price = bill_after_discount(total_price, 10)
        self.assertAlmostEqual(final_price, 20.611, places=2)

if __name__ == '__main__':
    unittest.main()
