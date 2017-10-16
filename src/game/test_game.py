import unittest
from unittest.mock import patch
import numpy as np
from game.game import build_grid, find_tile, find_empty_tile, movable_tiles, move, do_i_win, shuffle
from game.exception import MoveException, NoEmptyTileException, NoTileFoundException


class GameTest(unittest.TestCase):
    def test_build_grid_should_return_ordered_grid(self):
        self.assertTrue(np.array_equal(build_grid(), np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])))

    def test_find_tile_should_return_coords_of_a_tile(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 10, 11],
            [13, 14, 15, 12]
        ])
        self.assertEqual(find_tile(grid, 3), [0, 2])

    def test_find_tile_should_raise_exception_if_tile_not_in_grid(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        self.assertRaises(NoTileFoundException, find_tile, grid, 17)

    def test_find_empty_tile_should_return_coords_of_empty_tile(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 10, 11],
            [13, 14, 15, 12]
        ])
        self.assertEqual(find_empty_tile(grid), [2, 1])

    def test_find_empty_tile_exception_should_raise_exception_if_no_empty_tile_in_grid(self):
        not_valid_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        self.assertRaises(NoEmptyTileException, find_empty_tile, not_valid_grid)

    def test_movable_tiles_should_return_movable_tiles_from_a_grid(self):
        expected_movable_tiles = [12, 15]
        current_movable_tiles = movable_tiles(np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]))
        self.assertEqual(current_movable_tiles, expected_movable_tiles)

    def test_moves_should_make_two_moves(self):
        expected_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 0],
            [13, 14, 15, 12]
        ])
        grid = move(np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]), 12)
        self.assertTrue(np.array_equal(grid, expected_grid))

        expected_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ])
        grid = move(grid, 11)
        self.assertTrue(np.array_equal(grid, expected_grid))

    def test_moves_should_raise_exception_if_move_impossible(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        self.assertRaises(MoveException, move, grid, 7)
        self.assertTrue(np.array_equal(grid, np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])))

    def test_do_i_win_should_detect_victory(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        started_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        self.assertTrue(do_i_win(grid, started_grid))

    def test_do_i_win_should_not_detect_victory(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 0, 15]
        ])
        started_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        self.assertFalse(do_i_win(grid, started_grid))

    def test_shuffle_should_return_a_different_grid(self):
        started_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        expected_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 7, 11],
            [13, 14, 15, 12]
        ])
        with patch('game.game.move', return_value=expected_grid):
            grid = shuffle(started_grid)

        self.assertTrue(np.array_equal(grid, expected_grid))
        self.assertFalse(np.array_equal(grid, started_grid))
