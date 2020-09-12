from Grid import Grid
from Coordinate import Coordinate
from GridGenerator import NumericMatrixPopulator
from GridView import GridConsoleView
from Game import Game

def main():
    view = GridConsoleView( ' D ', ' A ' )
    generator = NumericMatrixPopulator([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ])
    game = Game(generator.generate())
    for i in range(5):
        game.nextIteration()
        view.print(game.getGrid())

if __name__ == "__main__":
    main()