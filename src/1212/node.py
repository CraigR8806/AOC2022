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
        self.cameFrom=None
        self.cachedMinFromHere=math.inf
        self.cachedChain=None

    def findit(self, cameFrom=None, costInit=0):
        costs=[]
        self.cameFrom=cameFrom
        self.cachedChain=None
        if self.cachedMinFromHere != math.inf:
            return costInit + self.cachedMinFromHere
        
        
        if self.pos == self.terrain.getEnd():
            self.terrain.setMinCostCache(costInit)
            return costInit

       
        chain=self.getCameFrom()
        

        for neighbor in self.neighbors:
            cost=costInit + self.calculateCost(neighbor)
            

            if cost >= self.terrain.getMinCostCache() or neighbor.getValue() - self.value > 1 or neighbor.pos in chain:
                continue
            neighborsShortestCost=neighbor.findit(self, cost)
            if neighborsShortestCost is not None:
                costs.append(neighborsShortestCost)
        
        
        if len(costs) <= 0:
            return None
        
        lowestCost=sorted(costs)[0]

        self.cachedMinFromHere=lowestCost-costInit

        if self.terrain.getMinCostCache() != math.inf:
            print()
        
        return lowestCost

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
        self.neighbors.sort(key=lambda n:math.sqrt(((n.pos[0]-self.terrain.getEnd()[0])**2) + ((n.pos[1]-self.terrain.getEnd()[1])**2)))

    
    def getValue(self):
        return self.value

    def getCameFrom(self):
        if self.cachedChain is not None:
            return self.cachedChain
        tmp=[]
        if self.cameFrom is not None:
            tmp=self.cameFrom.getCameFrom()
        tmp.append(self.pos)
        self.cachedChain=tmp[:]
    
        return tmp

    def __eq__(self, o):
        return self.pos == o.pos