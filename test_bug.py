import unittest
from my_adder import my_adder

class TestmyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(x=-5,y=3),-1)
