from distutils.errors import LibError
import unittest
from Game import Game
from Grid import Grid
from Cell import LiveCell, DeadCell
from GridView import GridConsoleView

#Here we test the known figures of the game: https://en.wikipedia.org/wiki/Conway's_Game_of_Life

class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_blinker(self):
        grid_blinker_initial = Grid(grid=
            [
                [DeadCell(), LiveCell(), DeadCell()],
                [DeadCell(), LiveCell(), DeadCell()],
                [DeadCell(), LiveCell(), DeadCell()],
            ]
        )
        grid_blinker_final = Grid(grid=
            [
                [DeadCell(), DeadCell(), DeadCell()],
                [LiveCell(), LiveCell(), LiveCell()],
                [DeadCell(), DeadCell(), DeadCell()],
            ]
        )

        game = Game(grid_blinker_initial)
        game.nextIteration()
        self.assertEqual(game.getGrid(), grid_blinker_final)

    def test_block(self):
        grid_block = Grid(grid=
            [
                [LiveCell(), LiveCell()],
                [LiveCell(), LiveCell()],
            ]
        )

        game = Game(grid_block)
        game.nextIteration()
        self.assertEqual(game.getGrid(), grid_block)

    def test_beacon(self):
        grid_beacon_initial = Grid(grid=
            [
                [LiveCell(), LiveCell(), DeadCell(), DeadCell()],
                [LiveCell(), LiveCell(), DeadCell(), DeadCell()],
                [DeadCell(), DeadCell(), LiveCell(), LiveCell()],
                [DeadCell(), DeadCell(), LiveCell(), LiveCell()],
            ]
        )
        grid_beacon_final = Grid(grid=
            [
                [LiveCell(), LiveCell(), DeadCell(), DeadCell()],
                [LiveCell(), DeadCell(), DeadCell(), DeadCell()],
                [DeadCell(), DeadCell(), DeadCell(), LiveCell()],
                [DeadCell(), DeadCell(), LiveCell(), LiveCell()],
            ]
        )

        game = Game(grid_beacon_initial)
        game.nextIteration()
        self.assertEqual(game.getGrid(), grid_beacon_final)

if __name__ == '__main__':
    unittest.main()