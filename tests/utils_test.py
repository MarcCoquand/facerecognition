import unittest
from src.Utils import *


class UtilsTest(unittest.TestCase):
    def test_mmult(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[2, 4, 6], [8, 10, 12]]
        self.assertEquals(mmult(m1, 2), m2)

    def test_msum(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        res = 21
        self.assertEquals(msum(m1), res)

    def test_mdot(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 4, 9, 16]
        self.assertEquals(ldot(l1, l1), l2)

    def test_flatten(self):
        l1 = [[1], [2], [3, 4], [5], [6], [7]]
        self.assertEquals(flatten(l1), [1, 2, 3, 4, 5, 6, 7])
