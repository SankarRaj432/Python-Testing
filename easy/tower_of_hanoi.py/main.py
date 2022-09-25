import unittest
from hanoi import Hanoi


class Test(unittest.TestCase):
    """ Tower of Hanoi Unit Tests """
    def empty_test(self):
        """ Empty Test """
        self.assertEqual(Hanoi(), 0)

    def negative_test(self):
        """ Negative Test """
        self.assertEqual(Hanoi(-1), 0)

    def test_hanoi(self):
        """ Test Tower of Hanoi """
        self.assertEqual(Hanoi(3), 7)

    def test_hanoi2(self):
        """ Test Tower of Hanoi """
        self.assertEqual(Hanoi(4), 15)

    def test_hanoi3(self):
        """ Test Tower of Hanoi """
        self.assertEqual(Hanoi(5), 31)

    def test_hanoi4(self):
        """ Test Tower of Hanoi """
        self.assertEqual(Hanoi(100), 2**100 - 1)

    

if __name__ == "__main__":
    unittest.main()