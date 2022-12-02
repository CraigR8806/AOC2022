
class Elf:



    def __init__(self, placeInLine:int, cals:list):
        self.placeInLine = placeInLine
        self.totalCals = sum(cals)

    def getPlaceInLine(self):
        return self.placeInLine

    def getTotalCals(self):
        return self.totalCals
        