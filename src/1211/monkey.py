import math

class Monkey:



    def __init__(self, startingItems:list, operation:str, monkeyLogic:str):
        self.items = [int(item) for item in startingItems]
        self.operation = operation.replace('old', 'self.items[0]').replace('new', 'self.items[0]')
        self.monkeyLogic=monkeyLogic
        self.inspectionCount=0

    def inspect(self):
        exec(self.operation)
        self.inspectionCount+=1

    def itemCount(self):
        return len(self.items)

    def evaluateMonkeyLogic(self):
        
        itemOut=int(self.items[0]/3)
        toMonkey=eval(self.monkeyLogic)
        self.items=self.items[1:]
        return itemOut, toMonkey

    def catchItem(self, item:int):
        self.items.append(item)

    def getInspectionCount(self):
        return self.inspectionCount


