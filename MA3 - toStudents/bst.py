""" bst.py

Student: Carl Agélii
Mail: calle.agelii01@gmail.com
Reviewed by: Stefanos Tsampanakis
Date reviewed: 2023-09-25
"""


from linked_list import LinkedList
import random
import math
from tabulate import tabulate
import numpy as np

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        def _height(r):
            if r == None:
                return 0
            return max(1+_height(r.left),1+_height(r.right))
        return _height(self.root)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right =  self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                temp = r.right
                while temp.left:
                    temp = temp.left
                # Put that key in this node
                r.key = temp.key
                # Remove that key from the right subtree
                r.right = self._remove(r.right,temp.key)
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        res = '<'
        for i in self:
            res += str(i) + ', '
        if res[-1] != '<':
            res = res[:-2]
        res += '>'
        return res

    def to_list(self):                            # Compulsory
        return [i for i in self] #complexity O(n)
            

    def to_LinkedList(self):                      # Compulsory
        res = LinkedList()
        for i in self:
            res.insert(i)
        return res #O(n^2)

    def ipl(self):                                # Compulsory
        def _ipl(r, n):
            if r == None:
                return 0
            return n + _ipl(r.left, n+1) + _ipl(r.right,n+1)
        return _ipl(self.root, 1)


def random_tree(n):                               # Useful
    tree = BST()
    r = random.Random()
    while n>tree.size():
        rand = r.random()
        tree.insert(rand)
    return tree


def main():
    # t = BST()
    # for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
    #     t.insert(x)
    # t.print()
    # print()

    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")

    ns = [500, 1000, 3000, 5000, 10000]
    data = np.zeros((len(ns),4))
    for i,n in enumerate(ns):
        random_t = random_tree(n)
        data[i] = np.array([n, round(1.39*math.log2(n),1),round(random_t.ipl()/n,1), random_t.height()])

    print (tabulate(data, headers=["n", "Theory", "IPL/n", "Height"]))


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
Pretty good since the entire tree needs to be run through.
2. computing height?
Not possible, since the height depends on the tree structure.
3. contains?
Works, but can in worst case take n computations. Using the tree structure is way more efficient.
4. insert?
Not really, since structure dependent. 
5. remove?
Not really since that could possible involve altering the tree and losing nodes. 


Results for ipl of random trees
===============================

    n    Theory    IPL/n    Height
-----  --------  -------  --------
  500      12.5     10.7        18
 1000      13.9     11.2        20
 3000      16.1     14.8        31
 5000      17.1     15.7        29
10000      18.5     16.6        34

Seems like the theoretical value is a bit higher. Also, the height seems to be approximately 2*IPL/n.

"""