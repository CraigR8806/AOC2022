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

    def findit(self, chainIn:list, costInit=0):
        chains=[]
        chainIn.append(self)
        if self.pos == self.terrain.getEnd():
            self.terrain.setMinCostCache(costInit)
            return chainIn
        for neighbor in self.neighbors:
            cost=costInit + self.calculateCost(neighbor)
            
            if cost >= self.terrain.getMinCostCache() or neighbor.getValue() - self.value > 1 or neighbor in chainIn:
                continue
            chainOut=copy(chainIn)
            neighborsShortestChain=neighbor.findit(chainOut, cost)
            if neighborsShortestChain is not None:
                chains.append(neighborsShortestChain)
        if len(chains) <= 0:
            return None
        cs=sorted(chains, key=lambda chain:sum([chain[i+1].calculateCost(chain[i]) for i in range(len(chain)-1)]))
        chainIn.extend(cs[0])
        if len(chains) > 1:
            print()
        tmp = set() 
        return [n for n in chainIn if n not in tmp and tmp.add(n) is None]

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

    def __eq__(self, o):
        return self.pos == o.pos