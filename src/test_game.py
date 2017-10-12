import unittest
from game import *


class GameTest(unittest.TestCase):

    def test_start(self):
        s = 'Welcome to the 15 puzzle game.'
        self.assertEqual(start(), s)

    def test_buildGrid(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.assertEqual(buildGrid(), grid)
