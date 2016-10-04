
class Examiner:
    """ Examiner  """

    def __init__(self, perceptrons, test_set):
        self.perceptrons = perceptrons
        self.test_set = test_set
        self.out_strings = []

    def examine(self):
        return map(self._make_guess, self.test_set)

    def _format_answer(self, img, guess):
        return "" + img.get_id() + " " + str(guess)

    def _make_guess(self, image):
        guess = {"type": 0, "activation": 0}
        for i in range(4):
            activation = self.perceptrons[i].process(image)
            if activation > guess["activation"]:
                guess["activation"] = activation
                guess["type"] = self.perceptrons[i].get_type_id()

        return self._format_answer(image, guess["type"])

    def _make_guess2(self, image):
        guess = {"type": 0, "activation": 0}
        guess = self._expose_perceptrons(image, guess, self.perceptrons)
        return self._format_answer(image, guess["type"])

    def _expose_perceptrons(self, image, current_guess, perceptrons):
        if not perceptrons: return current_guess
        activation = perceptrons[0].process(image)
        if activation > current_guess["activation"]:
            return self._update_guess(current_guess, activation, perceptrons[0])
        return current_guess

    def _update_guess(self, guess, activation, perceptron):
        g = guess
        g["activation"] = activation
        g["type"] = perceptron.get_type_id()
        return g
