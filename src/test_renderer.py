import unittest
from renderer import welcome, show_grid

DEFAULT_GRID = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class GameTest(unittest.TestCase):

    def test_start(self):
        msg = 'Welcome to the 15 puzzle game.'
        self.assertEqual(welcome(), msg)

    def test_render_grid(self):
        grid_rendered = """1    2    3    4    
5    6    7    8    
9    10   11   12   
13   14   15   0    
"""  # noqa
        self.assertEqual(show_grid(DEFAULT_GRID), grid_rendered)
