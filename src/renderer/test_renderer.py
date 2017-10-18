from unittest import TestCase
from renderer.renderer import (
    welcome, goodbye, shuffling, starting_turn,
    victory, show_action_not_valid,
    show_grid, show_moves, show_menu_size, show_size_not_valid,
    ask_move, ask_size
)


class GameTest(TestCase):

    def test_welcome_should_render_welcome_msg(self):
        msg = 'Welcome to the 15 puzzle game.'
        self.assertEqual(welcome(), msg)

    def test_goodbye_should_render_goodbye_msg(self):
        msg = 'Goodbye!'
        self.assertEqual(goodbye(), msg)

    def test_goodbye_should_render_goodbye_msg(self):
        msg = 'Shuffling the puzzle...'
        self.assertEqual(shuffling(), msg)

    def test_victory_should_render_victory_msg(self):
        msg = 'GGWP, you solved the puzzle in 5 turns!'
        self.assertEqual(victory(6), msg)

    def test_starting_turn_should_render_starting_msg(self):
        msg = 'Turn 12'
        self.assertEqual(starting_turn(12), msg)

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
        msg = 'You are allowed to move (12, 15)'
        self.assertEqual(show_moves([12, 15]), msg)

    def show_menu_size_should_render_menu_size_msg(self):
        msg = 'Press (W) to change the puzzle size, press any other key to use the default one: '
        self.assertEqual(show_menu_size('W'), msg)

    def test_size_not_valid_should_render_size_not_valid_error_msg(self):
        msg = 'Sorry, "hello" is not a valid size'
        self.assertEqual(show_size_not_valid('hello'), msg)

    def test_ask_move_should_render_ask_move_msg_without_shuffle_option(self):
        msg = 'Choose a tile to move: '
        self.assertEqual(ask_move(None, None), msg)

    def test_ask_move_should_render_ask_move_msg_with_only_shuffle_option(self):
        msg = 'Choose a tile to move or press (S) to shuffle: '
        self.assertEqual(ask_move(None, 'S'), msg)

    def test_ask_move_should_render_ask_move_msg_with_custom_keys(self):
        msg = 'Choose a tile to move or press (X) to resize or press (Y) to shuffle: '
        self.assertEqual(ask_move('X', 'Y'), msg)

    def test_ask_size_should_render_ask_size_msg_with_default_values(self):
        msg = 'Choose a new size (from 2 to 10): '
        self.assertEqual(ask_size(), msg)

    def test_ask_size_should_render_ask_size_msg_with_custom_values(self):
        msg = 'Choose a new size (from 4 to 8): '
        self.assertEqual(ask_size(4, 8), msg)
