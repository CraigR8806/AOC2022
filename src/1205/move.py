




class Move:


    def __init__(self, numberToMove, f, t):
        self.numberToMove = numberToMove
        self.f = f
        self.t = t

    def getNumberToMove(self):
        return self.numberToMove

    def getFrom(self):
        return self.f

    def getTo(self):
        return self.t