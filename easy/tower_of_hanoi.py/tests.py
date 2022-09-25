import unittest
import test_runner
from hanoi import Hanoi

class Test(unittest.TestCase):
    """ Tower of Hanoi Unit Tests """
    def test_hanoi_test_a(self):
        """ Normal Test 1"""
        self.assertEqual(Hanoi(3), 7, "Test 1 Failed")

    def test_hanoi_test_b(self):
        """ Normal Test 2"""
        self.assertEqual(Hanoi(4), 15, "Test 2 Failed")

    def test_hanoi_test_c(self):
        """ Normal Test 3"""
        self.assertEqual(Hanoi(5), 31, "Test 3 Failed")

    def test_hanoi_test_d(self):
        """ Normal Test 4"""
        self.assertEqual(Hanoi(100), 2**100 - 1, "Test 4 Failed")

    def test_hanoi_test_e(self):
        """ Exception Test 1"""
        self.assertEqual(Hanoi(0), 0, "Test 5 Failed")

    def test_hanoi_test_f(self):
        """ Exception Test 2"""
        self.assertEqual(Hanoi(-1), 1, "Test 6 Failed")

    def test_hanoi_test_g(self):
        """ Exception Test 3"""
        self.assertEqual(Hanoi("5"), 31, "Test 7 Failed")

    def test_hanoi_test_h(self):
        """ Exception Test 4"""
        self.assertEqual(Hanoi("a"), 1, "Test 8 Failed")

    def test_hanoi_test_i(self):
        """ Exception Test 5"""
        self.assertEqual(Hanoi(), 0, "Test 9 Failed")

    def test_hanoi_test_j(self):
        """ Exception Test 6"""
        self.assertEqual(Hanoi(1.5), 0, "Test 10 Failed")

if __name__ == "__main__":
    test_runner.main()