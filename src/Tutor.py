import random
from Utils import mmult


class Tutor:
    """ Tutor """

    def __init__(self, perceptrons, images, learning_rate, threshold):
        self.perceptrons = perceptrons
        self.images = images
        self.learning_rate = learning_rate
        self.threshold = threshold

    def train(self):
        # TODO: Implement without loops
        err_list = []
        while not self._accurate(err_list):
            err_list = []
            random.shuffle(self.images)
            for image in self.images:
                for perceptron in self.perceptrons:
                    err_list.append(self._expose(image, perceptron))
        return self

    def get_perceptrons(self):
        """
        get_perceptrons returns a tuple of perceptrons. This method returns
        the perceptrons in their current state. The train() method should be
        called until desired MSE is achieved before a call to this method
        makes sense
        :return: perceptrons as a tuple
        """
        return self.perceptrons

    def _expose(self, image, perceptron):
        act = perceptron.process(image)
        out = self._desired_out(image, perceptron)
        err = self._error(out, act)
        dw = self._delta_weight(image, err)
        perceptron.update_weight(dw)
        # print perceptron.get_type_id(), act, image.get_ans()
        return err

    def _delta_weight(self, inp, err):
        """
        Uses the formula (error * learning rate * input) from lecture notes
        to produce the delta error for the activation of the perceptron
        which is returned
        :param inp: the perceptron input (image)
        :param out: desired output, either 0 or 1
        :param act: the activation of the perceptron
        :return:
        """
        return mmult(inp.get_img(), self.learning_rate * err)

    def _error(self, out, act):
        return out - act

    def _accurate(self, err_list):
        if not err_list: return False
        mse = (sum(map(lambda x: x**2, err_list)))/2
        print mse
        return mse < self.threshold

    def _desired_out(self, img, percept):
        """
        Compares the provided image and perceptron to determine whether
        the neuron should be firing on the image. The decision is
        represented as either 0 or 1
        :return: 1 or 0 if the neuron should fire
        """
        return int(img.get_ans() == percept.get_type_id())
