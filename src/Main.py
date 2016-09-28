import sys
import re
from Enum import Enum
from Perceptron import Perceptron
from Tutor import Tutor
from Examiner import Examiner
from Image import Image

# Program arguments: training-set, answer-set, examination-set (from spec)
EXPECTED_ARGS = 3
Types = Enum(["HAPPY", "SAD", "MISCHIEVOUS", "MAD"])


def parse_facit(facit_file):
    facit = open(facit_file, 'r')
    facits = []
    for line in facit:
        if re.search('Image', line) is not None:
            answer = [int(s) for s in re.findall(r'\b\d+\b', line)]
            facits.append(answer)
    return facits


def parse_img_file(image_file):
    image = open(image_file, 'r')
    images = []
    for line in image:
        if re.search('Image', line) is not None:
            img_gen = []
            for line2 in image:
                if len(line2) != 1:
                    img_gen.append(line2)
                else:
                    images.append(Image(img_gen))
                    break
    return images


def main():
    # Since program name is provided as additional first argument
    if len(sys.argv) < EXPECTED_ARGS + 1:
        print "This program expects exactly %d args. %d was provided" % (EXPECTED_ARGS, len(sys.argv) - 1)
        sys.exit(0)

    # Define our different perceptrons and put in a tuple
    happy = Perceptron(Types.HAPPY)
    sad = Perceptron(Types.SAD)
    mischievous = Perceptron(Types.MISCHIEVOUS)
    mad = Perceptron(Types.MAD)
    perceptrons = (happy, sad, mischievous, mad)

    # use our tutor to train our perceptrons on a training set
    tutor = Tutor(perceptrons, [])
    tutor.train()

    # examine our perceptrons
    examiner = Examiner(tutor.get_trained_perceptrons())

if __name__ == "__main__":
    main()
