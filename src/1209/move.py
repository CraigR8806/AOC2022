
class Move:

    def __init__(self, direction:str, steps:int):
        self.direction = (1,0) if direction=="R" else (-1,0) if direction=="L" else \
                         (0,1) if direction=="D" else (0,-1)
        self.steps = int(steps)+1

    @classmethod
    def fromTuple(cls, directionAndSteps:tuple):
        return cls(directionAndSteps[0], directionAndSteps[1])


    def getDirection(self):
        return self.direction

    def isDone(self):
        self.steps-=1
        return self.steps<=0

    def __str__(self):
        return self.direction + " " + str(self.steps)

    