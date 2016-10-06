import random
from Utils import mmult, flatten


class Tutor:
    """
    Tutor represents a supervisor object that is responsible for training a
    set of perceptrons using a provided set of training images until a
    certain level of correctness is reached.
    Attributes:
        perceptrons: a tuple of perceptrons to train
        images: a list of image objects to train on
        learning_rate: value specifying how quickly the network should learn
        threshold: the value that indicates when to stop training
    """

    def __init__(self, perceptrons, images, learning_rate, threshold):
        self.perceptrons = perceptrons
        self.images = images
        self.learning_rate = learning_rate
        self.threshold = threshold

    def train(self):
        """
        Trains the perceptrons provided to this object with the provided
        using the provided training images until the desired threshold
        for the sum squared error of the network is reached. The trained
        perceptrons are returned as a tuple.
        """
        self._do_training([])
        return self.perceptrons

    def _do_training(self, errors):
        """
        This function is what actually does what's described in the train
        method. This separation is done so that the user of this method is
        not bothered by the fact that the method is implemented recursively.
        """
        if self._accurate(errors): return self
        random.shuffle(self.images)
        self._do_training(flatten(map(self._each_perceptron, self.images)))

    def _each_perceptron(self, image):
        """
        Shows the provided image to all the perceptrons and returns a list
        containing the error for every perceptron.
        """
        return map(lambda p: self._expose(image, p), self.perceptrons)

    def get_perceptrons(self):
        """
        get_perceptrons returns a tuple of perceptrons. This method returns
        the perceptrons in their current state. The train() method should be
        called until desired MSE is achieved before a call to this method
        makes sense.
        :return: perceptrons as a tuple
        """
        return self.perceptrons

    def _expose(self, image, perceptron):
        """
        Shows the provided image to the specific perceptron and uses the
        formula for perceptron learning from lecture notes to update the
        internal weights in the perceptron based on the delta error
        for the perceptron on the image.
        :return:
        """
        err = self._error(self._desired(image, perceptron), perceptron.process(image))
        dw = self._delta_weight(image, err)
        perceptron.update_weight(dw)
        return err

    def _delta_weight(self, inp, err):
        """
        Uses the formula (error * learning rate * input) from lecture notes
        to produce the delta error for the activation of the perceptron
        which is returned.
        :param inp: the perceptron input (image)
        :param out: desired output, either 0 or 1
        :param act: the activation of the perceptron
        :return:
        """
        return mmult(inp.get_img(), self.learning_rate * err)

    def _error(self, out, act):
        """
        Computes the error between the desired output and the actual activation
        """
        return out - act

    def _accurate(self, err_list):
        """
        Determines the size of the error using the formula for computing
        the error of a network provided over at:
        http://lcn.epfl.ch/tutorial/english/perceptron/html/learning.html
        Uses the user provided threshold value to determine whether the
        network performs well enough.
        """
        if not err_list: return False
        mse = (sum(map(lambda x: x**2, err_list)))/2
        return mse < self.threshold

    def _desired(self, img, percept):
        """
        Compares the provided image and perceptron to determine whether
        the neuron should be firing on the image. The decision is
        represented as either 0 or 1.
        :return: 1 or 0 if the neuron should fire
        """
        return int(img.get_ans() == percept.get_type_id())
