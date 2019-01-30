import unittest
from src.calc2 import Calc as clc

class CalcTst(unittest.TestCase):
    def test_add(self):
        self.assertEqual(clc.add(2, 6), 18)