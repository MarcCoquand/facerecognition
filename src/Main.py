import sys
import re
from Enum import Enum
from Perceptron import Perceptron
from Tutor import Tutor
from Utils import flatten
from Examiner import Examiner
from Image import Image

# Program arguments: training-set, answer-set, examination-set (from spec)
EXPECTED_ARGS = 3
Types = Enum(["HAPPY", "SAD", "MISCHIEVOUS", "MAD"])


def parse_ans(ans_file):
    """
     Opens the provided answer file and extracts the answers which are returned
     as a list of integers.
    :param ans_file: path to answer file
    :return: list of integers
    """
    l2 = filter(lambda l: len(l) > 0, map(lambda line: get_answer(line), open(ans_file, 'r')))
    return flatten(l2)


def parse_img_file(image_file):
    image = open(image_file, 'r')
    images = []
    for line in image:
        if re.search('Image', line) is not None:
            img_gen = extract_img_data(20, image)
            for line2 in image:
                if len(line2) != 1:
                    img_gen.append(line2)
                else:
                    images.append(Image(format_img_row(img_gen)))
                    break
    return images


def extract_img_data(acc, i):
    return []


def format_img_row(img):
    """
    format_img_row receives a row from the image file representing a pixel
    row in an image and returns it as a list of floats in [0,1)
    :param img: image pixel row
    :return: list of integers
    """
    return map(lambda l: map(lambda i: (float(i)/100), l), map(lambda i: i.rstrip().split(' '), img))


def get_answer(line):
    """
    get_answer retrieves the value for the answer from a line in the
    answer file
    :param line: line from answer file
    :return: Integer representing the answer for the line
    """
    return map(lambda s: int(s), re.findall(r'\b\d+\b', line))


def main():
    # Since program name is provided as additional first argument
    if len(sys.argv) < EXPECTED_ARGS + 1:
        print "This program expects exactly %d args. %d was provided" % (EXPECTED_ARGS, len(sys.argv) - 1)
        sys.exit(0)

    # Define our different perceptrons and put in a tuple
    perceptrons = (Perceptron(Types.HAPPY), Perceptron(Types.SAD),
                   Perceptron(Types.MISCHIEVOUS), Perceptron(Types.MAD))

    img_list = parse_img_file(sys.argv[1])
    ans_list = parse_ans(sys.argv[2])

    # Link image and answer
    images = map(lambda ans: img_list.pop(0).set_ans(ans), ans_list)

    # use our tutor to train our perceptrons on a training set
    tutor = Tutor(perceptrons, images).train()

    # examine our perceptrons
    Examiner(tutor.get_trained_perceptrons())

if __name__ == "__main__":
    main()
