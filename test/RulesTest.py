import unittest
from Rules import Rules

class TestRules(unittest.TestCase):
    def setUp(self) -> None:
        self.rules = Rules()
        self.isAlive = True
        self.isDead = False
        super().setUp()

    def test_shouldLive_liveCell_WithZeroLiveNeighbors(self):
        self.assertFalse(self.rules.shouldLive(self.isAlive, 0))

    def test_shouldLive_liveCell_WithOneLiveNeighbors(self):
        self.assertFalse(self.rules.shouldLive(self.isAlive, 1))

    def test_shouldLive_liveCell_WithTwoLiveNeighbors(self):
        self.assertTrue(self.rules.shouldLive(self.isAlive, 2))

    def test_shouldLive_liveCell_WithThreeLiveNeighbors(self):
        self.assertTrue(self.rules.shouldLive(self.isAlive, 3))

    def test_shouldLive_liveCell_WithFourLiveNeighbors(self):
        self.assertFalse(self.rules.shouldLive(self.isAlive, 4))

    def test_shouldLive_DeadCell_WithZeroLiveNeighbors(self):
        self.assertFalse(self.rules.shouldLive(self.isDead, 0))

    def test_shouldLive_DeadCell_WithOneLiveNeighbors(self):
        self.assertFalse(self.rules.shouldLive(self.isDead, 1))

    def test_shouldLive_DeadCell_WithThreeLiveNeighbors(self):
        self.assertTrue(self.rules.shouldLive(self.isDead, 3))

if __name__ == '__main__':
    unittest.main()