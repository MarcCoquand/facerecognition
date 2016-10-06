
class Examiner:
    """
    Examiner is a class that, provided a set of trained neurons and
    test images, examines the training results of the network
    Attributes:
        perceptrons: tuple of trained perceptrons
        test_set: set of test images

    """

    def __init__(self, perceptrons, test_set):
        self.perceptrons = perceptrons
        self.test_set = test_set

    def examine(self):
        """
        Tests the provided perceptrons on the provided set of images
        :return: A list of formatted answer strings
        """
        return map(self._make_guess, self.test_set)

    def _make_guess(self, image):
        """
        Exposes the provided image to the network and returns a string
        that is compliant with the specification of what a guess should
        look like
        :return:
        """
        guess = self._expose_perceptrons(image, {"type": 0, "activation": 0}, self.perceptrons)
        return self._format_answer(image, guess["type"])

    def _expose_perceptrons(self, image, current_guess, perceptrons):
        """
        Shows an image to all of the perceptrons and returns the largest
        activation from the network
        :param image: image to show
        :param current_guess: The previous largest activation in the network
        :param perceptrons: consumed list of perceptrons
        :return:
        """
        if not perceptrons: return current_guess
        activation = perceptrons[0].process(image)
        if activation > current_guess["activation"]:
            current_guess = self._update_guess(activation, perceptrons[0])

        return self._expose_perceptrons(image, current_guess, perceptrons[1:])

    def _update_guess(self, activation, perceptron):
        """
        Returns a new dictionary containing the activation for the
        perceptron type
        """
        return {"type": perceptron.get_type_id(), "activation": activation}

    def _format_answer(self, img, guess):
        """
        Returns properly formatted string based on the networks guess of
        the provided image
        """
        return "" + img.get_id() + " " + str(guess)
