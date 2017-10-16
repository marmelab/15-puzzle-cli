from unittest import TestCase
from renderer.renderer import welcome, goodbye, show_action_not_valid, show_grid, show_moves, ask_move


class GameTest(TestCase):

    def test_welcome_should_render_welcome_msg(self):
        msg = 'Welcome to the 15 puzzle game.'
        self.assertEqual(welcome(), msg)

    def test_goodbye_should_render_goodbye_msg(self):
        msg = 'Goodbye!'
        self.assertEqual(goodbye(), msg)

    def test_show_action_not_valid_should_display_error(self):
        msg = '"Hello" is not a valid action'
        self.assertEqual(show_action_not_valid('Hello'), msg)

    def test_show_grid_should_render_grid(self):
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

    def test_show_moves_should_render_possible_moves_msg(self):
        msg = 'You are allowed to move: 12 15 '
        self.assertEqual(show_moves([12, 15]), msg)

    def test_ask_move_should_render_ask_move_msg_without_shuffle_option(self):
        msg = 'Choose a tile to move: '
        self.assertEqual(ask_move(True), msg)

    def test_ask_move_should_render_ask_move_msg_witt_shuffle_option(self):
        msg = 'Choose a tile to move or press (S) to shuffle: '
        self.assertEqual(ask_move(False), msg)
