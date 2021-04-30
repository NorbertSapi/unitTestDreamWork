import unittest
from dream_work import *


class MyTestCase(unittest.TestCase):

    def test_decoder(self):

        self.assertListEqual(decoder(sample1), expected_list1)
        self.assertListEqual(decoder(sample2), expected_list2)
        self.assertListEqual(decoder(sample3), expected_list3)
        self.assertListEqual(decoder(sample4), expected_list4)


if __name__ == '__main__':
    unittest.main()
