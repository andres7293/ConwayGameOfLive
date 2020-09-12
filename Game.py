from Cell import Cell
from Grid import Grid
from Rules import Rules
from Coordinate import Coordinate
import copy

class Game():
    def __init__(self, grid: Grid = None):
        self.rules: Rules = Rules()
        self.grid: Grid = grid
        self.grid_copy: Grid = None

    def nextIteration(self) -> None:
        self.grid_copy = copy.deepcopy(self.grid)
        self.grid.iterate(self.__gridIterator)
        self.grid = self.grid_copy

    def getGrid(self) -> Grid:
        return self.grid

    def __gridIterator(self, r: int, c: int, cell: Cell, grid: Grid) -> None:
        coordinate = Coordinate(r, c)
        numLiveNeighbours = grid.getNumAliveNeighbours(coordinate)
        if (self.rules.shouldLive(cell.isAlive(), numLiveNeighbours)):
            self.grid_copy.getCell(coordinate).born()
        else:
            self.grid_copy.getCell(coordinate).kill()