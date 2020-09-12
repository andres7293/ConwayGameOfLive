from Cell import Cell, DeadCell
from Coordinate import Coordinate

class CellMatrixSize(Coordinate):
    def __init__(self, row: int, column: int):
        super().__init__(row, column)

class CellMatrix:
    def __init__(self, row: int = 0, column: int = 0, cellmatrix: list = None):
        if not cellmatrix:
            self._row = row
            self._column = column
            self.__createEmptyGrid()
        else:
            self._row    = len(cellmatrix)
            self._column = len(cellmatrix[0])
            self._cellmatrix = cellmatrix

    def __createEmptyGrid(self):
        cellmatrix = []
        for r in range(0, self._row):
            column = []
            for c in range(0, self._column):
                column.append(DeadCell())
            cellmatrix.append(column)
        self._cellmatrix = cellmatrix

    def isOutOfBound(self, coordinate: Coordinate) -> bool:
        if coordinate.row < 0 or coordinate.column < 0:
            return True
        elif coordinate.row >= self._row or coordinate.column >= self._column:
            return True
        else:
            return False

    def getCell(self, coordinate: Coordinate) -> Cell:
        return self._cellmatrix[coordinate.row][coordinate.column]

    def getSize(self) -> CellMatrixSize:
        return CellMatrixSize(self._row, self._column)