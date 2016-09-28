
class Tutor:
    """ Tutor """

    def __init__(self, perceptrons, images):
        self.perceptrons = perceptrons
        self.images = images

    def train(self):
        for perceptron in self.perceptrons:
            for i in range(len(self.images)):
                print perceptron.process(self.images)

    def get_trained_perceptrons(self):
        return self.perceptrons

    def evaluate_output(self, output, perceptron, img):
        return
