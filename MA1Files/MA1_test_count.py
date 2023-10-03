# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        lst = [1,1,2,3,4,[4,5]]
        print('\nTests count')
        print('\nTests empty list')
        self.assertEqual(count(1,[]), 0)
        print('\nTests first and last element')
        self.assertEqual(count(1,lst), 2)
        self.assertEqual(count(5,lst), 1)
        print('\nTest if it is possible to search for lists')
        self.assertEqual(count([4,5],lst), 1)
        print('\nTry searching for non-existing element')
        self.assertEqual(count(8,lst), 0)

        self.assertEqual(count(4,lst), 2)
        print('\nSee if list is intact')
        self.assertEqual(lst, [1,1,2,3,4,[4,5]])


if __name__ == "__main__":
    unittest.main()
