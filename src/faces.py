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

# Optimal values (derived from experiments):
# learning_rate = 0.01
# threshold = 1
LEARNING_RATE = 0.1
THRESHOLD = 1


def parse_ans(ans_file):
    """
    Opens the provided answer file and extracts the answers which are
    returned as a list of integers. NON PURE FUNCTION!
    :param ans_file: path to answer file
    :return: list of integers
    """
    l2 = filter(lambda l: len(l) > 0, map(get_answer, open(ans_file, 'r')))
    return flatten(l2)


def parse_img_file(image_file):
    """
    Opens the provided image file and extracts its content into a
    list of image objects that gets returned. NON PURE FUNCTION!
    :return: list of image objects
    """
    f = open(image_file, 'r')
    return reduce_img_file(f.readlines(), [])


def reduce_img_file(lines, images):
    """
    Consumes the lines of the image file in order to extract all
    the images and their ids. In the end it will return a list
    of image objects.
    :return: list om image objects
    """
    if not lines: return images
    if re.search('Image', lines[0]) is not None:
        img = Image(extract_img_data(20, lines[1:]))
        return reduce_img_file(lines[20:], images + [img.set_id(lines[0])])

    return reduce_img_file(lines[1:], images)


def extract_img_data(acc, lines):
    """
    Sub consumes all the lines that contains an image row and
    returns a 2D array containing list of lists of integers
    :param acc: int representing how many more lines to read
    :param lines: the lines of the file
    :return: 2D array of integers
    """
    if acc == 1: return [format_img_row(lines[0])[0]]
    return [format_img_row(lines[acc-1])[0]] + extract_img_data(acc - 1, lines)


def format_img_row(row):
    """
    format_img_row receives a row from the image file representing a pixel
    row in an image and returns it as a list of floats in [0,1)
    :param row: image pixel row
    :return: list of integers
    """
    if isinstance(row, list):
        print row
    return map(lambda l: map(lambda i: (float(i)/31), l), map(lambda i: i.rstrip().split(' '), [row]))


def get_answer(line):
    """
    get_answer retrieves the value for the answer from a line in the
    answer file
    :param line: line from answer file
    :return: Integer representing the answer for the line
    """
    return map(lambda s: int(s), re.findall(r'\b\d+\b', line))


def validate_arguments():
    """
    makes sure that the user provided the right amount of arguments to the
    program, else: fail gracefully. NON PURE FUNCTION!
    :return:
    """
    # Since program name is provided as additional first argument
    if len(sys.argv) < EXPECTED_ARGS + 1:
        print "This program expects exactly %d args. %d was provided" % \
              (EXPECTED_ARGS, len(sys.argv) - 1)
        sys.exit(0)


def print_results(res_arr):
    """
    Expects a list with formatted answer strings that gets printed to stdout
    """
    if not res_arr: return
    print res_arr[0]
    print_results(res_arr[1:])


def main():
    validate_arguments()
    perceptrons = (Perceptron(Types.HAPPY), Perceptron(Types.SAD),
                   Perceptron(Types.MISCHIEVOUS), Perceptron(Types.MAD))

    # Get content of the data files
    img_list = parse_img_file(sys.argv[1])
    ans_list = parse_ans(sys.argv[2])
    test_set = parse_img_file(sys.argv[3])

    # Link image and answer
    images = map(lambda ans: img_list.pop(0).set_ans(ans), ans_list)

    trained_p = Tutor(perceptrons, images, LEARNING_RATE, THRESHOLD).train()
    print_results(Examiner(trained_p, test_set).examine())

if __name__ == "__main__":
    main()
