from unittest import TestCase
from unittest.mock import patch
from renderer.renderer import welcome, goodbye, show_grid, show_moves, ask_move


class GameTest(TestCase):

    def test_welcome(self):
        msg = 'Welcome to the 15 puzzle game.'
        self.assertEqual(welcome(), msg)

    def test_goodbye(self):
        msg = 'Goodbye!'
        self.assertEqual(goodbye(), msg)

    def test_show_grid(self):
        grid_rendered = """
|-------------------|
|  1 |  2 |  3 |  4 |
|-------------------|
|  5 |  6 |  7 |  8 |
|-------------------|
|  9 | 10 | 11 | 12 |
|-------------------|
| 13 | 14 | 15 |    |
|-------------------|
"""  # noqa
        grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        self.assertEqual(show_grid(grid), grid_rendered)

    def test_show_moves(self):
        msg = 'You are allowed to move: 12 15 '
        self.assertEqual(show_moves([12, 15]), msg)

    def test_ask_move(self):
        msg = 'Choose a tile to move: '
        self.assertEqual(ask_move(), msg)
