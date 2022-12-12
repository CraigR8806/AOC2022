from copy import deepcopy
from functools import reduce


class Node:



    def __init__(self, x:int, y:int, value:int, terrain):
        self.pos=(y, x)
        self.value = value
        self.neighbors = []
        self.terrain = terrain

    def findit(self, chainIn:list):
        chains=[]
        chainIn.append(self)
        if self.pos == self.terrain.getEnd():
            return chainIn
        for neighbor in self.neighbors:
            chainOut=deepcopy(chainIn)
            if neighbor.getValue() - self.value > 1 or neighbor in chainIn:
                continue
            neighborsShortestChain=neighbor.findit(chainOut)
            if neighborsShortestChain is not None:
                chains.append(neighborsShortestChain)
        if len(chains) <= 0:
            return None

        chainIn.extend(sorted(chains, key=lambda x:reduce(lambda a, b:a.calculateCost(b), x), reverse=True)[0])
        print(chainIn)
        return chainIn

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
        
            

    def calculateCost(self, next):
        delta=next.getValue() - self.value 
        return delta if delta >= 0 else 0

    def getPos(self):
        return self.pos

    def getX(self):
        return self.pos[1]

    def getY(self):
        return self.pos[0]


    
    def getValue(self):
        return self.value

    def __eq__(self, o):
        return self.pos == o.pos