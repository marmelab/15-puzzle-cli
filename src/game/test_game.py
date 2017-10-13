import unittest
import numpy as np
from game.Move import Move
from game.game import build_grid, find_empty_tile, possible_moves, move
from game.exception import MoveException, NoEmptyTileException


class GameTest(unittest.TestCase):
    def test_build_grid(self):
        self.assertTrue(np.array_equal(build_grid(), np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])))

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

    def test_possible_moves(self):
        expected_possible_moves = [Move.TOP, Move.LEFT]
        current_moves = possible_moves(np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]))
        self.assertEqual(current_moves, expected_possible_moves)

    def test_moves(self):
        expected_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 0],
            [13, 14, 15, 12]
        ])
        expected_possible_moves = [Move.TOP, Move.BOTTOM, Move.LEFT]
        grid = move(np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]), Move.TOP)
        self.assertTrue(np.array_equal(grid, expected_grid))
        self.assertEqual(possible_moves(grid), expected_possible_moves)

        expected_grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ])
        expected_possible_moves = [Move.TOP, Move.RIGHT, Move.BOTTOM, Move.LEFT]
        grid = move(grid, Move.LEFT)
        self.assertTrue(np.array_equal(grid, expected_grid))
        self.assertEqual(possible_moves(grid), expected_possible_moves)

    def test_moves_impossible(self):
        grid = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])
        self.assertRaises(MoveException, move, grid, Move.BOTTOM)
        self.assertTrue(np.array_equal(grid, np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ])))
