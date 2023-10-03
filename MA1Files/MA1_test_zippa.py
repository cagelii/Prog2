# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_zippa(self):
        print('\nTests zippa')
        self.assertEqual(zippa(['a', 'b', 'c'], [2, 4, 6, 'x', 10]), ['a', 2, 'b', 4, 'c', 6, 'x', 10])
        self.assertEqual(zippa([],[1,2,3]),[1,2,3])
        self.assertEqual(zippa([1,2,3],[]),[1,2,3])
        self.assertEqual(zippa([1,2,3],[1,2]),[1,1,2,2,3])
        self.assertEqual(zippa([1,2],[1,2,3]),[1,1,2,2,3])
        self.assertEqual(zippa([1,2,3],[1,2,3]),[1,1,2,2,3,3])


if __name__ == "__main__":
    unittest.main()
