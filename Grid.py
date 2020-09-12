from Cell import Cell, LiveCell, DeadCell
from CellMatrix import CellMatrix, CellMatrixSize
from Coordinate import Coordinate

class Grid(CellMatrix):
    def __init__(self, row: int = 0, column: int = 0, grid: CellMatrix = None):
        super().__init__(row=row, column=column, cellmatrix=grid)

    def getNumAliveNeighbours(self, coordinate: Coordinate) -> int:
        assert self.isOutOfBound(coordinate) == False

        nbCoordinates = self.__getNeighboursCoordinate(coordinate)
        numAliveNb = 0
        for nb in nbCoordinates:
            if not self.isOutOfBound(nb) and self.isCellAlive(nb):
                numAliveNb += 1
        return numAliveNb

    def getNumDeadNeighbours(self, coordinate: Coordinate) -> int:
        return 8 - self.getNumAliveNeighbours(coordinate)

    def iterate(self, func) -> None:
        for r in range(self._row):
            for c in range(self._column):
                func(r, c, self._cellmatrix[r][c], self)

    def isCellAlive(self, coordinate: Coordinate) -> bool:
        return self.getCell(coordinate).isAlive()

    def __getNeighboursCoordinate(self, coordinate: Coordinate) -> list:
        i = coordinate.row
        j = coordinate.column
        return [
            Coordinate(i - 1, j),
            Coordinate(i - 1, j - 1),
            Coordinate(i - 1, j + 1),
            Coordinate(i, j - 1),
            Coordinate(i, j + 1),
            Coordinate(i + 1, j - 1),
            Coordinate(i + 1, j),
            Coordinate(i + 1, j + 1)
        ]

    def __eq__(self, other: object) -> bool:
        for r in range(self._row):
            for c in range(self._column):
                selfCell = self._cellmatrix[r][c]
                otherCell = other._cellmatrix[r][c]
                if selfCell.isAlive() != otherCell.isAlive():
                    return False
        return True