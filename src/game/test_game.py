import unittest
import numpy as np
from game.game import build_grid, find_tile, find_empty_tile, movable_tiles, move
from game.exception import MoveException, NoEmptyTileException, NoTileFoundException


class GameTest(unittest.TestCase):
    def test_build_grid(self):
        self.assertTrue(np.array_equal(build_grid(), np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])))

    def test_find_tile(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 10, 11],
            [13, 14, 15, 12]
        ])
        self.assertEqual(find_tile(grid, 3), [0, 2])

    def test_find_tile_exception(self):
        not_valid_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        self.assertRaises(NoTileFoundException, find_tile, not_valid_grid, 17)

    def test_find_empty_tile(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 10, 11],
            [13, 14, 15, 12]
        ])
        self.assertEqual(find_empty_tile(grid), [2, 1])

    def test_find_empty_tile_exception(self):
        not_valid_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])
        self.assertRaises(NoEmptyTileException, find_empty_tile, not_valid_grid)

    def test_movable_tiles(self):
        expected_movable_tiles = [12, 15]
        current_movable_tiles = movable_tiles(np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]))
        self.assertEqual(current_movable_tiles, expected_movable_tiles)

    def test_moves(self):
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

    def test_moves_impossible(self):
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
