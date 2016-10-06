import unittest
from src.Utils import *


class UtilsTest(unittest.TestCase):
    def test_mmult(self):
        m1 = [1, 2, 3, 4, 5, 6]
        m2 = [2, 4, 6, 8, 10, 12]
        self.assertEquals(mmult(m1, 2), m2)

    def test_msum(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        res = 21
        self.assertEquals(msum(m1), res)

    def test_flatten(self):
        l1 = [[1], [2], [3, [4]], [[[5], [6]], [7]]]
        self.assertEquals(flatten(l1), [1, 2, 3, 4, 5, 6, 7])

    def test_flatten_flat_array(self):
        l1 = [1, 2, 3, 4, 5]
        self.assertEquals(l1, l1)

    def test_flatten_nested_flat_array(self):
        l1 = [[[[1, 2, 3, 4]]]]
        self.assertEquals(flatten(l1), [1, 2, 3, 4])

    def test_apply(self):
        l1 = [1, 2, 3, 4]
        l2 = [1, 4, 9, 16]
        add = float.__add__
        self.assertEquals(apply(add, l1, l2), [2, 6, 12, 20])
