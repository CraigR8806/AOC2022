import math

class Monkey:



    def __init__(self, startingItems:list, operation:str, monkeyLogic:str):
        self.items = [str(item) for item in startingItems]
        self.operation = operation.replace('old', 'self.items[0]').replace('new', 'self.items[0]')
        self.monkeyLogic=monkeyLogic

    def inspect(self):
        exec(self.operation)

    def itemCount(self):
        return len(self.items)

    def evaluateMonkeyLogic(self):
        toMonkey=eval(self.monkeyLogic)
        itemOut=int(self.items[0]/3)
        self.items=self.items[1:]
        return itemOut, toMonkey

    def catchItem(self, item:int):
        self.items.append(item)


