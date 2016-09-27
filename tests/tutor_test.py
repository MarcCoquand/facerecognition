import unittest
from src.Perceptron import Perceptron
from src.Tutor import Tutor


class TutorTest(unittest.TestCase):
    def test_train(self):
        p1 = Perceptron("HAPPY")
        p2 = Perceptron("SAD")
        t = Tutor((p1, p2), [])
        t.train()
