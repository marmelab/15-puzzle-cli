from unittest import TestCase
from unittest.mock import patch
from renderer.renderer import welcome, goodbye, show_grid, show_moves, ask_move
from game.Move import Move

DEFAULT_GRID = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


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
        self.assertEqual(show_grid(DEFAULT_GRID), grid_rendered)

    def test_show_moves(self):
        msg = 'You are allowed to go: (T)op (L)eft '
        self.assertEqual(show_moves([Move.TOP, Move.LEFT]), msg)

    def test_ask_move(self):
        accepted_values = [
            ['T', Move.TOP],
            ['R', Move.RIGHT],
            ['B', Move.BOTTOM],
            ['L', Move.LEFT],
            ['A', None]
        ]
        for value in accepted_values:
            with patch('builtins.input', return_value=value[0]):
                self.assertEqual(ask_move(), value[1])
            with patch('builtins.input', return_value=value[0].lower()):
                self.assertEqual(ask_move(), value[1])
