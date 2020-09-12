def DeadCell():
    return Cell(isAlive=False)

def LiveCell():
    return Cell(isAlive=True)
class Cell():
    def __init__(self, isAlive=False):
        self._isAlive = isAlive

    def isAlive(self) -> bool:
        return self._isAlive

    def isDead(self) -> bool:
        return not self._isAlive

    def kill(self) -> None:
        self._isAlive = False

    def born(self) -> None:
        self._isAlive = True