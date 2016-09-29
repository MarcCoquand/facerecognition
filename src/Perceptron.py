import random
import math
from Utils import *

TYPES = {"HAPPY": 1, "SAD": 2, "MISCHIEVOUS": 3, "MAD": 4}


class Perceptron:
    """
        Perceptron represents a perceptron object that is
        used to fire based
    """

    def __init__(self, percept_type):
        self.percept_type = percept_type
        self.bias = random.random()
        self.weights = self._generate_weights(19, 19, 19)
        self.type_id = TYPES[percept_type]

    def process(self, img):
        l1 = ldot(flatten(img.get_img()), self.weights)
        return self.act(sum(l1))

    def act(self, val):
        return 1 / (1 + math.exp(-val))

    def update_weight(self, dw):
        self.weights = ldot(flatten(dw), self.weights)

    def get_type(self):
        return self.percept_type

    def get_type_id(self):
        return self.type_id

    def _generate_weights(self, rows, cols, tot):
        if rows == 0 and cols == 0:
            return [random.random()]

        if cols == 0:
            return self._generate_weights(rows-1, tot, tot) + [random.random()]

        return self._generate_weights(rows, cols-1, tot) + [random.random()]
