from abc import ABC, abstractmethod

class FSO(ABC):

    def __init__(self, name:str, isadir=False):
        self.name = name
        self.isadir = isadir


    @abstractmethod
    def getSize(self, recursive=True):
        pass

    def isDir(self):
        return self.isadir

    def getName(self):
        return self.name