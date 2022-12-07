from fso import FSO


class File(FSO):


    def __init__(self, name:str, size:int):
        self.fsos = []
        self.size = int(size)
        super().__init__(name)


    def getSize(self, recursize=True):
        return self.size