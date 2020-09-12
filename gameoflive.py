import sys
import copy

class GameOfLive:
    def __init__(self, world, rows, cols):
        self.world = world
        self.rows = rows
        self.cols = cols

    def play(self, iterations=10):
        self.__printGame()
        while iterations > 0:
            new_world = self.nextGeneration()
            self.world = copy.deepcopy(new_world)
            self.__printGame()
            iterations -= 1

    def nextGeneration(self):
        new_world = copy.deepcopy(self.world)
        for i in range(self.rows):
            for j in range(self.cols):
                numNb = self.countLiveNeighbours(i, j)
                if self.isAlive(i, j):
                    if numNb < 2:
                        new_world[i][j] = 0
                    elif numNb == 2 or numNb == 3:
                        new_world[i][j] = 1
                    elif numNb > 3:
                        new_world[i][j] = 0
                else:
                    if numNb == 3:
                        new_world[i][j] = 1
        return new_world

    def isAlive(self, i, j):
        if self.world[i][j] == 1:
            return True
        else:
            return False

    def countLiveNeighbours(self, i, j):
        count = 0
        nbList = self.getNeighbours(i, j)
        for (ni, nj) in nbList:
            if self.isInsideWorld(ni, nj):
                if self.world[ni][nj]:
                    count += 1
        return count

    def getNeighbours(self, i, j):
        return [(i - 1, j), (i - 1, j - 1), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

    def isInsideWorld(self, i, j):
        if (i >= 0 and i < self.rows) and (j >= 0 and j < self.cols):
            return True
        else:
            return False

    def __printGame(self):
        sys.stdout.write('\n')
        for i in range(self.rows):
            sys.stdout.write('\n')
            for j in range(self.cols):
                if self.world[i][j]:
                    sys.stdout.write(' # ')
                else:
                    sys.stdout.write(' . ')

world=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
        ]

g = GameOfLive(world, len(world), len(world[0]))
g.play(50)
