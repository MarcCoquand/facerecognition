
class Tutor:
    """ Tutor """

    def __init__(self, perceptrons, images):
        self.perceptrons = perceptrons
        self.images = images

    def train(self):
        for perceptron in self.perceptrons:
            for i in range(1):
                print perceptron.process(self.images[i])

    def get_trained_perceptrons(self):
        return self.perceptrons

    def evaluate_output(self, output, perceptron, img):
        return
