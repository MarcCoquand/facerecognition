
class Examiner:
    """ Examiner  """

    def __init__(self, perceptrons, test_set):
        self.perceptrons = perceptrons
        self.test_set = test_set
        self.out_strings = []

    def examine(self):
        # TODO: Implement without loops
        for image in self.test_set:
            guess = self._expose_network(image)
            self._append_answer(image, guess)
        self._write_answer()

    def _append_answer(self, img, guess):
        self.out_strings.append("" + img.get_id() + " " + str(guess))

    def _write_answer(self):
        map(lambda line: self._print_line(line), self.out_strings)

    def _expose_network(self, image):
        # TODO: Implement without loops
        guess = {"type": 0, "activation": 0}
        for i in range(4):
            activation = self.perceptrons[i].process(image)
            if activation > guess["activation"]:
                guess["activation"] = activation
                guess["type"] = self.perceptrons[i].get_type_id()

        return guess["type"]

    def _print_line(self, line):
        print line
