import unittest
from game import build_grid


class GameTest(unittest.TestCase):

    def test_build_grid(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.assertEqual(build_grid(), grid)
