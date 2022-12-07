from functools import reduce
from fso import FSO


class Dir(FSO):


    def __init__(self, name:str):
        self.fsos = []
        super().__init__(name, True)


    def addFSO(self, fso:FSO):
        self.fsos.append(fso)

    def getChild(self, name:str):
        try:
            return [self.fsos[i] for i in range(len(self.fsos)) if self.fsos[i].getName() == name][0]
        except:
            return None


    def getSize(self, recursive=True):
        return sum([fso.getSize() for fso in self.fsos if recursive == True or not fso.isDir()])
    