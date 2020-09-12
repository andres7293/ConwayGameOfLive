import unittest
from CellMatrix import CellMatrix, CellMatrixSize
from Cell import Cell, DeadCell, LiveCell
from Coordinate import Coordinate

class CellMatrixTest(unittest.TestCase):

    def test_is_out_of_bounds(self):
        matrix = CellMatrix(row=5, column=5)
        self.assertTrue(matrix.isOutOfBound(Coordinate(10, 10)))
        self.assertTrue(matrix.isOutOfBound(Coordinate(-1, -1)))
        self.assertTrue(matrix.isOutOfBound(Coordinate(1, 6)))
        self.assertTrue(matrix.isOutOfBound(Coordinate(6, 1)))

    def test_get_size(self):
        for i in range(0, 10):
            matrix = CellMatrix(i, i)
            self.assertEqual(matrix.getSize().row, i)
            self.assertEqual(matrix.getSize().column, i)

    def test_get_cell(self) :
        matrix = CellMatrix(cellmatrix=[[DeadCell(), LiveCell(), DeadCell()]])
        self.assertTrue(matrix.getCell(Coordinate(0, 0)).isDead())
        self.assertTrue(matrix.getCell(Coordinate(0, 1)).isAlive())
        self.assertTrue(matrix.getCell(Coordinate(0, 2)).isDead())
