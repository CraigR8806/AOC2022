from copy import copy, deepcopy
from functools import reduce
import math


class Node:



    def __init__(self, x:int, y:int, value:int, terrain):
        self.pos=(y, x)
        self.value = value
        self.neighbors = []
        self.terrain = terrain
        self.cachedMinFromHere=math.inf
        self.cachedChainFromHere=[]

    def findit(self, chainIn:list, cameFrom=None, costInit=0):
        costs=[]
        if self.cachedMinFromHere != math.inf:
            self.terrain.clearNodesVisited()
            # self.terrain.addPath(deepcopy(chainIn))
            return costInit + self.cachedMinFromHere
        self.terrain.addNodeVisited(self.pos)
        
        if self.pos == self.terrain.getEnd():
            self.terrain.setMinCostCache(costInit)
            self.terrain.clearNodesVisited()
            self.terrain.addPath(deepcopy(chainIn))
            return costInit
        

        for neighbor in self.neighbors:
            cost=costInit + self.calculateCost(neighbor)
            

            if cost >= self.terrain.getMinCostCache() or neighbor.getValue() - self.value > 1 or neighbor.pos in self.terrain.getNodesVisited() or neighbor.pos in chainIn:
                continue
            chainIn.append(self.pos)
            neighborsShortestCost=neighbor.findit(chainIn, self, cost)
            chainIn.pop()
            if neighborsShortestCost is not None:
                costs.append(neighborsShortestCost)
        
        
        if len(costs) <= 0:
            return None
        
        lowestCost=sorted(costs)[0]

        self.cachedMinFromHere=lowestCost-costInit
        
        return lowestCost

    def getX(self):
        return self.pos[1]

    def getY(self):
        return self.pos[0]

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def calculateCost(self, prev):
        prevV=prev
        if isinstance(prev, Node):
            prevV=prev.getValue()

        delta=self.value - prevV
        return 1

    def sortNeighbors(self):
        self.neighbors.sort(key=lambda n:math.sqrt(((n.pos[0]-self.terrain.getEnd()[0])**2) + ((n.pos[1]-self.terrain.getEnd()[1])**2)))

    def getValue(self):
        return self.value