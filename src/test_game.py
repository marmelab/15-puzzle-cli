import unittest
from game import Move, build_grid, possible_moves, move


class GameTest(unittest.TestCase):
    def test_build_grid(self):
        self.assertEqual(build_grid(), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

    def test_possible_moves(self):
        expected_possible_moves = [Move.TOP, Move.LEFT]
        self.assertEqual(possible_moves([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]), expected_possible_moves)

    def test_moves(self):
        expected_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]]
        expected_possible_moves = [Move.TOP, Move.BOTTOM, Move.LEFT]
        grid = move([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], Move.TOP)
        self.assertEqual(grid, expected_grid)
        self.assertEqual(possible_moves(grid), expected_possible_moves)

        expected_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]]
        expected_possible_moves = [Move.TOP, Move.RIGHT, Move.BOTTOM, Move.LEFT]
        grid = move(grid, Move.LEFT)
        self.assertEqual(grid, expected_grid)
        self.assertEqual(possible_moves(grid), expected_possible_moves)

    def test_moves_impossible(self):
        grid = move([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], Move.BOTTOM)
        self.assertEqual(grid, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])        
