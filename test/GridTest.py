from os import setgid
import unittest

from Grid import Grid
from Coordinate import Coordinate
from Cell import DeadCell, LiveCell

class TestGrid(unittest.TestCase):

    def test_grid_size(self):
        for i in range(0, 10):
            grid = Grid(i, i)
            size = grid.getSize()
            self.assertEqual(size.row, i)
            self.assertEqual(size.column, i)
    
    def test_grid_is_created_with_dead_cells(self):
        grid = Grid(10, 10)
        size = grid.getSize()
        for i in range(size.row):
            for j in range(size.column):
                self.assertEqual(grid.getCell(Coordinate(i, j)).isAlive(), False)
    
    def test_is_out_of_bounds(self):
        grid = Grid(10, 10)
        self.assertTrue(grid.isOutOfBound(Coordinate(10, 10)))
        self.assertTrue(grid.isOutOfBound(Coordinate(-1, -1)))
        self.assertFalse(grid.isOutOfBound(Coordinate(0, 0)))
        self.assertFalse(grid.isOutOfBound(Coordinate(9, 9)))
    
    def test_get_cell(self):
        customGrid = [
            [DeadCell(), LiveCell(), DeadCell()],
        ]
        grid = Grid(grid=customGrid)
        self.assertEqual(grid.getCell(Coordinate(0, 0)).isAlive(), False)
        self.assertEqual(grid.getCell(Coordinate(0, 1)).isAlive(), True)

    def test_num_neighbours(self):
        customGrid = [
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), LiveCell(), DeadCell()],
        ]
        grid = Grid(grid=customGrid)
        self.assertEqual(grid.getNumAliveNeighbours(Coordinate(0, 0)), 2)
        self.assertEqual(grid.getNumDeadNeighbours(Coordinate(0, 0)), 8 - 2)

        self.assertEqual(grid.getNumAliveNeighbours(Coordinate(0, 1)), 1)
        self.assertEqual(grid.getNumDeadNeighbours(Coordinate(0, 1)), 8 - 1)

        self.assertEqual(grid.getNumAliveNeighbours(Coordinate(1, 1)), 2)
        self.assertEqual(grid.getNumDeadNeighbours(Coordinate(1, 1)), 8 - 2)

    def test_iterate(self):
        customGrid = [
            [LiveCell(), DeadCell(), LiveCell()],
            [LiveCell(), DeadCell(), LiveCell()],
            [LiveCell(), DeadCell(), LiveCell()],
            [LiveCell(), DeadCell(), LiveCell()],
            [LiveCell(), LiveCell(), LiveCell()],
            [LiveCell(), LiveCell(), LiveCell()],
            [LiveCell(), DeadCell(), LiveCell()],
        ]
        grid = Grid(grid=customGrid)
        grid.iterate(lambda r, c, cell, grid: self.assertEqual(cell.isAlive(), customGrid[r][c].isAlive()))
    
    # Create a grid of dead cells. Choose one and born it
    # then check if the cell is alive.
    def test_createDeadCell_then_bornCell(self):
        customGrid = [
            [DeadCell(), DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
        ]
        grid = Grid(grid=customGrid)

        for i in range(0, len(customGrid)):
            for j in range(0, len(customGrid[0])):
                coordinate = Coordinate(i, j)
                self.assertTrue(grid.getCell(coordinate).isDead())
                grid.getCell(coordinate).born()
                self.assertTrue(grid.getCell(coordinate).isAlive())


if __name__ == '__main__':
    unittest.main()
