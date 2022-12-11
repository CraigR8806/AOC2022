import math

class Monkey:



    def __init__(self, startingItems:list, operation:str, test:str, testT:str, testF:str):
        self.items = [int(item) for item in startingItems]
        self.operation = operation.replace('old', 'self.items[0]').replace('new', 'self.items[0]')
        self.inspectionCount=0

        self.divisor=test
        self.monkeyLogic = str(testT) + " if itemOut%" + str(test) + "==0 else "  + str(testF)

    def inspect(self, leastCommonMultiple:int, partTwo=False):
        exec(self.operation)
        if partTwo:
            self.items[0] = self.items[0] % leastCommonMultiple
        self.inspectionCount+=1

    def itemCount(self):
        return len(self.items)

    def evaluateMonkeyLogic(self, partTwo=False):
        
        itemOut=self.items[0]
        if not partTwo:
            itemOut=int(itemOut/3)
        toMonkey=eval(self.monkeyLogic)
        self.items=self.items[1:]
        return itemOut, toMonkey

    def catchItem(self, item:int):
        self.items.append(item)

    def getInspectionCount(self):
        return self.inspectionCount

    def getDivisor(self):
        return int(self.divisor)

