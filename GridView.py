from Grid import Grid
from Coordinate import Coordinate
from Cell import Cell

class GridConsoleView():
    def __init__(self, deadCaracter = "   ", aliveCaracter = " X "):
        self.deadCaracter = deadCaracter
        self.aliveCaracter = aliveCaracter

    def print(self, grid) -> None:
        print(self.getString(grid))

    def __str__(self) -> str:
        return self.getString()

    def getString(self, grid) -> str:
        output = ''
        for r in range(grid.getSize().row):
            for c in range(grid.getSize().column):
                if grid.getCell(Coordinate(r, c)).isAlive():
                    output += self.aliveCaracter
                else:
                    output += self.deadCaracter
            output += "\n"
        return output