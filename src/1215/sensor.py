




class Sensor:


    def __init__(self, pos:tuple, cbPos:tuple):
        self.pos = pos
        self.cbPos = cbPos

        self.distFromBeacon = abs(pos[0] - cbPos[0]) + abs(pos[1] - cbPos[1])


    def getManahattanDistance(self):
        return self.distFromBeacon

    def getPosition(self):
        return self.pos

    def getClosestBeaconPosition(self):
        return self.cbPos

    def modifyPosition(self, delta:tuple):
        self.pos=(self.pos[0] + delta[0], self.pos[1] + delta[1])

    def modifyBeaconPosition(self, delta:tuple):
        self.cbPos=(self.cbPos[0] + delta[0], self.cbPos[1] + delta[1])