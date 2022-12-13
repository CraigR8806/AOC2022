from node import Node
from copy import deepcopy
import math





class Terrain:



    def __init__(self, grid):
        for i, line in enumerate(grid):
            try:
                self.start = (i, line.index(-1))
            except:
                pass
            try:
                self.end = (i, line.index(-2))
            except:
                pass
        grid[self.start[0]][self.start[1]] = 0
        grid[self.end[0]][self.end[1]] = 25

        self.grid=[]
        for y in range(len(grid)):
            self.grid.append([])
            for x in range(len(grid[y])):
                self.grid[y].append(Node(x, y, grid[y][x], self))

        for y in range(len(self.grid)):
            for node in self.grid[y]:
                nx=node.getX()
                ny=node.getY()
                maxY=len(self.grid)
                maxX=len(self.grid[y])
                if nx > 0:
                    node.addNeighbor(self.grid[ny][nx-1])
                if ny > 0:
                    node.addNeighbor(self.grid[ny-1][nx])
                if nx < maxX-1:
                    node.addNeighbor(self.grid[ny][nx+1])
                if ny < maxY-1:
                    node.addNeighbor(self.grid[ny+1][nx])

                node.sortNeighbors()

        self.costCache = math.inf
        self.nodesVisited=[]
        self.paths = []

    # def __getitem__(self, indicies):
    #     if not isinstance(indicies, tuple):
    #         indicies = tuple(indicies)

    #     return self.grid[indicies[0]][indicies[1]]

    def findShortestPath(self):
        return self.grid[self.start[0]][self.start[1]].findit([])

    def findShortestPathFromStartingHeight(self, startingHeight:int):
        distances=[]
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x].getValue() == startingHeight:
                    distances.append(self.grid[y][x].findit([]))

        return sorted(distances)[0]

    def getEnd(self):
        return self.end
        
    def setMinCostCache(self, cost:int):
        self.costCache = cost

    def getMinCostCache(self):
        return self.costCache

    def getNodesVisited(self):
        return self.nodesVisited

    def addNodeVisited(self, node):
        self.nodesVisited.append(node)

    def clearNodesVisited(self):
        self.nodesVisited.clear()

    def addPath(self, chain:list):
        self.paths.append(chain)

    def compileAndSavePaths(self):
        origBoard = [list(map(lambda x:chr(x.getValue()+97), line)) for line in self.grid]

        for path in self.paths:
            outBoard=deepcopy(origBoard)
            for point in path:
                outBoard[point[0]][point[1]] = "*"

            print("\n".join(["".join(line) for line in outBoard]))

        print(len(self.paths))