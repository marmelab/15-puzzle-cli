import unittest
from unittest.mock import patch
from game.random import random_move


class RandomTest(unittest.TestCase):
    def test_random_move(self):
        values = [7, 11, 15, 10]
        with patch('random.sample', return_value=[values[1]]):
            self.assertEqual(random_move(values), values[1])
