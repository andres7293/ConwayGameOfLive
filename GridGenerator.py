from Grid import Grid
from Grid import Coordinate
import random

class Populator:
    def __init__(self):
        pass

    def populate():
        pass

class NumericMatrixPopulator(Populator):
    def __init__(self, matrix: list):
        self._matrix: int = matrix
        self.maxrow: int = len(matrix)
        self.maxcolumn: int = len(matrix[0])
        self.grid: Grid = None

    def generate(self) -> Grid:
        self.grid = Grid(self.maxrow, self.maxcolumn)
        for r in range(self.maxrow):
            for c in range(self.maxcolumn):
                if self._matrix[r][c] == 1:
                    self.grid.getCell(Coordinate(r, c)).born()
                else:
                    self.grid.getCell(Coordinate(r, c)).kill()
        return self.grid

class RandomPopulator(Populator):
    def __init__(self, row: int, column: int):
        self.row: int = row
        self.column: int = column
        self.grid: int = Grid(self.row, self.column)

    def generate(self) -> Grid:
        for r in range(self.row):
            for c in range(self.column):
                if bool(random.getrandbits(1)):
                    self.grid.getCell(Coordinate(r, c)).born()
                else:
                    self.grid.getCell(Coordinate(r, c)).kill()
        return self.grid