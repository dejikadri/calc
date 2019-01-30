import unittest
from src.calc import Calc as clc

class CalcTst(unittest.TestCase):
    def test_add(self):
        self.assertEquals(clc.add(2, 6), 18)