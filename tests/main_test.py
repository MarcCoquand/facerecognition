import unittest
from src.Main import *

TRAINING_FILE = "../data/training.txt"


class MainTest(unittest.TestCase):

    def test_parse_img_file(self):
        img_list = parse_img_file(TRAINING_FILE)
        self.assertNotEquals(len(img_list), 0)
        for i in range(len(img_list)):
            self.assertTrue(isinstance(img_list[i], Image([]).__class__))

    def test_parse_facit(self):
        return
