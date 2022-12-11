from copy import deepcopy
from monkey import Monkey
from functools import reduce
import math
import re


def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def findLeastCommonMultiple(divisors:list)->int:
    out=max(divisors)
    while not all([out % divisor == 0 for divisor in divisors]):
        out+=1
    return out



def parseDemMonkies(lines):
    monkies=[]
    monkeyInfo={}
    for line in lines:
        monkeyNumberM=re.findall("(?<=^Monkey )([0-9]+)(?=:)", line)
        startingItemsM="".join(re.findall("(?<=^  Starting items: )(.+)", line)).split(", ")
        operationM=re.findall("(?<=^  Operation: )(.+)", line)
        testM=re.findall("(?<=^  Test: divisible by )([0-9]+)", line)
        testTM=re.findall("(?<=^    If true: throw to monkey )([0-9]+)", line)
        testFM=re.findall("(?<=^    If false: throw to monkey )([0-9]+)", line)


        if len(monkeyNumberM) > 0:
            monkeyInfo['number'] = monkeyNumberM[0]
        if startingItemsM[0] != "":
            monkeyInfo['startingItems'] = startingItemsM
        if len(operationM) > 0:
            monkeyInfo['operation'] = operationM[0]
        if len(testM) > 0:
            monkeyInfo['test'] = testM[0]
        if len(testTM) > 0:
            monkeyInfo['testT'] = testTM[0]
        if len(testFM) > 0:
            monkeyInfo['testF'] = testFM[0]

        if len(monkeyInfo) == 6:
            monkies.append(Monkey(monkeyInfo['startingItems'], monkeyInfo['operation'], monkeyInfo['test'], monkeyInfo['testT'], monkeyInfo['testF']))
            monkeyInfo.clear()

    return monkies

def processRounds(rounds:int, monkies:list, partTwo=False):

    divisors=[monkey.getDivisor() for monkey in monkies]
    leastCommonMultiple=findLeastCommonMultiple(divisors)

    for round in range(rounds):
        for monkey in monkies:
            for items in range(monkey.itemCount()):
                monkey.inspect(leastCommonMultiple, partTwo)
                item,toMonkey=monkey.evaluateMonkeyLogic(partTwo)
                monkies[toMonkey].catchItem(item)

    monkeyBusiness=reduce(lambda a,b:a.getInspectionCount()*b.getInspectionCount(), sorted(monkies, key=lambda x:x.getInspectionCount(), reverse=True)[:2])
    return monkeyBusiness

sampleMonkies=parseDemMonkies(getStripedLinesFromFile('src/1211/sampleInput.data'))
monkies=parseDemMonkies(getStripedLinesFromFile('src/1211/input.data'))
print(processRounds(20, deepcopy(sampleMonkies)))
print(processRounds(20, deepcopy(monkies)))

print(processRounds(10000, deepcopy(sampleMonkies), True))
print(processRounds(10000, deepcopy(monkies), True))