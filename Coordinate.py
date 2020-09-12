class Coordinate():
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def __str__(self):
        return "row={},column={}".format(self.row, self.column)