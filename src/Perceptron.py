import random
from Utils import *


class Perceptron:
    """
        Perceptron represents a perceptron object that is
        used to fire based
    """

    def __init__(self, percept_type):
        self.percept_type = percept_type
        self.bias = random.random()
        self.threshold = random.random()

    def process(self, img):
        m1 = mmult(img, self.bias)
        return msum(m1)

    def update(self, new_bias):
        self.bias = new_bias

    def get_type(self):
        return self.percept_type
