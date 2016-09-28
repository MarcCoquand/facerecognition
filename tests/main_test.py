import unittest
from src.Main import *

TRAINING_FILE = "../data/training.txt"
TRAINING_FILE_ANS = "../data/training-facit.txt"


class MainTest(unittest.TestCase):

    def test_parse_img_file(self):
        img_list = parse_img_file(TRAINING_FILE)
        self.assertNotEquals(len(img_list), 0)
        for i in range(len(img_list)):
            self.assertTrue(isinstance(img_list[i], Image([]).__class__))

    def test_parse_ans(self):
        ans_list = parse_ans(TRAINING_FILE_ANS)
        self.assertNotEquals(len(ans_list), 0)
        self.assertEquals(ans_list[0], 2)
        self.assertEquals(ans_list[12], 3)
