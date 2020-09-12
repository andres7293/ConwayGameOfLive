import unittest
from Cell import Cell, DeadCell
from Cell import LiveCell

class TestCell(unittest.TestCase):
    def test_isAlive(self):
        cell = Cell()
        self.assertFalse(cell.isAlive())
        cell.born()
        self.assertTrue(cell.isAlive())
        cell.kill()
        self.assertFalse(cell.isAlive())

    def test_isDead(self):
        cell = Cell()
        self.assertTrue(cell.isDead())
        cell.born()
        self.assertFalse(cell.isDead())
        cell.kill()
        self.assertTrue(cell.isDead())

    def test_LiveCell(self):
        cell = LiveCell()
        self.assertTrue(cell.isAlive())
        cell.kill()
        self.assertFalse(cell.isAlive())
        cell.born()
        self.assertTrue(cell.isAlive())

    def test_DeadCell(self):
        cell = DeadCell()
        self.assertTrue(cell.isDead())
        cell.born()
        self.assertTrue(cell.isAlive())

if __name__ == '__main__':
    unittest.main()