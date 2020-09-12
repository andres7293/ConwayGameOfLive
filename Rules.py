class Rules():
    def __init__(self):
        pass

    def shouldLive(self, isCellAlive, numLiveNeighbors) -> bool:
        if isCellAlive:
            return self.__shouldAliveCellLive(numLiveNeighbors)
        else:
            return self.__shouldDeadCellLive(numLiveNeighbors)

    def shouldDie(self, isCellAlive, numLiveNeighbors) -> bool:
        return not self.shouldLive(isCellAlive, numLiveNeighbors)

    def __shouldAliveCellLive(self, numLiveNeighbors) -> bool:
            if numLiveNeighbors == 2 or numLiveNeighbors == 3:
                return True
            else:
                return False

    def __shouldDeadCellLive(self, numLiveNeighbors) -> bool:
            if numLiveNeighbors == 3:
                return True
            else:
                return False