import unittest
from game import *

class GameTest(unittest.TestCase):

    def test_start(self):
        s = 'Welcome to the 15 puzzle game.'
        self.assertEqual(start(), s)
