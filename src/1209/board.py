

class Board:


    def __init__(self, length:int, startX=0, startY=0):
        self.start=(startX, startY)
        self.knots=[self.start for i in range(length)]
        self.knotUnique=[set([knot]) for knot in self.knots]
        self.length=length

    def xy(self, index):
        return self.knots[index]

    def moveKnot(self, index:int, xy:tuple):
        self.knots[index]=xy
        self.knotUnique[index].add(xy)

    def getUniqueKnotPositions(self, index:int):
        return self.knotUnique[index]

    def getLength(self):
        return self.length

    def __str__(self):
        out=[]
        boardSize=26
        for i in range(boardSize):
            out.append([])
            for j in range(boardSize):
                n=None
                for k in range(self.length):
                    if self.knots[k][0]==j-boardSize/2 and self.knots[k][1]==i-boardSize/2:
                        n="H" if k==0 else "T" if k==self.length-1 else k
                        break
                out[i].append(str(n) if n is not None else "s" if self.start[0] == j-boardSize/2 and self.start[1] == i-boardSize/2 else ".")
        return "\n".join(["".join(o) for o in out])