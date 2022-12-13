from copy import copy
from functools import reduce
import math


class Node:



    def __init__(self, x:int, y:int, value:int, terrain):
        self.pos=(y, x)
        self.value = value
        self.neighbors = []
        self.terrain = terrain
        self.hash=hash(self.pos)
        self.chain=[]

    def findit(self, chainIn:list, costInit=0):
        costs=[]
        # print(chainIn)
        self.chain.extend(chainIn)
        
        if self.pos == self.terrain.getEnd():
            self.terrain.setMinCostCache(costInit)
            return costInit

        chainIn.append(self.pos)
        for neighbor in self.neighbors:
            cost=costInit + self.calculateCost(neighbor)
            if cost >= self.terrain.getMinCostCache() or neighbor.getValue() - self.value > 1 or neighbor.pos in self.chain:
                continue
            neighborsShortestCost=neighbor.findit(chainIn, cost)
            if neighborsShortestCost is not None:
                costs.append(neighborsShortestCost)
        
        self.chain = []
        
        if len(costs) <= 0:
            return None
        chainIn.remove(self.pos)
        
        return sorted(costs)[0]

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
        
            

    def calculateCost(self, prev):
        prevV=prev
        if isinstance(prev, Node):
            prevV=prev.getValue()

        delta=self.value - prevV
        return 1

    def getPos(self):
        return self.pos

    def getX(self):
        return self.pos[1]

    def getY(self):
        return self.pos[0]

    def __hash__(self):
        return self.hash

    def sortNeighbors(self):
        # self.neighbors.sort(key=lambda n:(n.getValue(), math.sqrt(((n.pos[0]-self.terrain.getEnd()[0])**2) + ((n.pos[1]-self.terrain.getEnd()[1])**2))), reverse=True)
        self.neighbors.sort(key=lambda n:math.sqrt(((n.pos[0]-self.terrain.getEnd()[0])**2) + ((n.pos[1]-self.terrain.getEnd()[1])**2)))
        if self.pos == (20,3):
            [print(math.sqrt(((n.pos[0]-self.terrain.getEnd()[0])**2) + ((n.pos[1]-self.terrain.getEnd()[1])**2))) for n in self.neighbors]

    
    def getValue(self):
        return self.value

    def __eq__(self, o):
        return self.pos == o.pos