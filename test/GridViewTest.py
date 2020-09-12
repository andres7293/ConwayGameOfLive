import unittest
from GridView import GridConsoleView
from Grid import Grid
from Cell import Cell, LiveCell, DeadCell

class TestGridConsoleView(unittest.TestCase):

    def test_print_pattern1(self):
        input = [
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), LiveCell(), DeadCell()],
        ]
        result = "DAD\nDAD\nDAD\n"
        grid = Grid(grid=input)
        view = GridConsoleView("D", "A")
        self.assertEqual(view.getString(grid), result)
    
    def test_print_pattern2(self):
        input = [
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
        ]
        result = "DAD\nDDD\nDDD\n"
        grid = Grid(grid=input)
        view = GridConsoleView("D", "A")
        self.assertEqual(view.getString(grid), result)

    def test_print_pattern3(self):
        input = [
            [DeadCell(), LiveCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(), DeadCell()],
            [LiveCell(), LiveCell(), LiveCell()],
            [LiveCell(), LiveCell(), LiveCell()],
            [LiveCell(), LiveCell(), LiveCell()],
        ]
        result = "DAD\nDDD\nDDD\nAAA\nAAA\nAAA\n"
        grid = Grid(grid=input)
        view = GridConsoleView("D", "A")
        self.assertEqual(view.getString(grid), result)

if __name__ == '__main__':
    unittest.main()
