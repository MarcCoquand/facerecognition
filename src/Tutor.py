from Utils import mmult, flatten

class Tutor:
    """ Tutor """

    def __init__(self, perceptrons, images):
        self.perceptrons = perceptrons
        self.images = images
        self.learning_rate = 0.001

    def train(self):
        # for perceptron in self.perceptrons:
        #     for i in range(self.images):
        #         perceptron.process(self.images[i])
                # perceptron.update(delta_weight(x, y, perceptron.process(self.images[i])))
        perceptron = self.perceptrons[0]
        for i in range(len(self.images)):
            image = self.images[i]
            act = perceptron.process(image)
            dw = self.delta_weight(image, self.desired_out(image, perceptron), act)
            perceptron.update_weight(dw)
            print act
        return self

    def get_trained_perceptrons(self):
        return self.perceptrons

    def delta_weight(self, inp, out, act):
        err = out - act
        return mmult(inp.get_img(), self.learning_rate*err)

    def desired_out(self, img, percept):
        return int(img.get_ans() == percept.get_type_id())
