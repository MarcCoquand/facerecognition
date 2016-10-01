import random
import math
from Utils import *


class Perceptron:
    """
        Perceptron
    """

    def __init__(self, percept_type):
        self.TYPES = {"HAPPY": 1, "SAD": 2, "MISCHIEVOUS": 3, "MAD": 4}
        self.bias = random.random()
        self.weights = self._generate_weights(400)
        self.type_id = self.TYPES[percept_type]

    def process(self, img):
        """
        Uses the formula sum(w[i], x[i]) from lecture notes to process an image
        :return: summed weight of inputs
        """
        l1 = apply(float.__mul__, flatten(img.get_img()), self.weights)
        return self._act(sum(l1))

    def _act(self, val):
        """
        Computes the activation for the perceptron based on the sum of the
        weighted input
        :param val: summed weight in input
        :return: activation of the perceptron
        """
        return 1 / (1 + math.exp(-val))

    def update_weight(self, dw):
        """
        adds the provided delta error for the last iteration to each
        value in the internal weight matrix according to lecture notes
        :return: None
        """
        self.weights = apply(float.__add__, flatten(dw), self.weights)

    def get_type_id(self):
        """
        Returns the type id for this perceptron. Consult the type
        type attribute for explanation of the meaning of the returned
        value.
        :return: type id as an integer [1, 4]
        """
        return self.type_id

    def _generate_weights(self, acc):
        """
        Returns a list of the specified length containing pseudo
        random values in interval [0.0, 1.0)
        :param acc: length of the list to generate
        :return: list of pseudo random floats
        """
        return [random.random()] if acc == 1 else self._generate_weights(acc-1) + [random.random()]
