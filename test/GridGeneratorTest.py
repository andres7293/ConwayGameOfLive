import unittest
from Cell import Cell, DeadCell, LiveCell
from Grid import Grid
from Coordinate import Coordinate
from GridGenerator import NumericMatrixPopulator

class TestNumericMatrixPopulator(unittest.TestCase):

    def test_generate(self):
        matrix = [
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 1],
        ]
        expected_grid = Grid(grid=[
            [DeadCell(), LiveCell(), DeadCell(), DeadCell(), LiveCell()],
            [DeadCell(), LiveCell(), DeadCell(), DeadCell(), LiveCell()],
            [DeadCell(), LiveCell(), DeadCell(), DeadCell(), LiveCell()],
        ])
        populator = NumericMatrixPopulator(matrix)
        self.assertEqual(populator.generate(), expected_grid)

if __name__ == '__main__':
    unittest.main()