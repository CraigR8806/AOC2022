






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
        self.grid=grid

    def __getitem__(self, indicies):
        if not isinstance(indicies, tuple):
            indicies = tuple(indicies)

        return self.grid[indicies[0]][indicies[1]]


    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end
        