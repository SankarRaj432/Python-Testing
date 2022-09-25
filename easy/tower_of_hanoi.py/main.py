import unittest
from hanoi import Hanoi


class Test(unittest.TestCase):
    """ Tower of Hanoi Unit Tests """
    def test_hanoi(self):
        """ Test Tower of Hanoi """
        self.assertEqual(Hanoi(3), 7)