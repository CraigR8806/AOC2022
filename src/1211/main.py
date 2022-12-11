from monkey import Monkey
import math
import re


def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
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
            monkies.append(Monkey(monkeyInfo['startingItems'], monkeyInfo['operation'], str(monkeyInfo['testT']) + " if int(math.modf(int(self.items[0])/int(" + str(monkeyInfo['test']) + "))[0])==0 else "  + str(monkeyInfo['testF'])))
            monkeyInfo.clear()

    return monkies

def processRounds(rounds:int, monkies:list):
    for round in range(rounds):
        for monkey in monkies:
            for items in range(monkey.itemCount()):
                monkey.inspect()
                item,toMonkey=monkey.evaluateMonkeyLogic()
                monkies[toMonkey].catchItem(item)

    for monkey in monkies:
        print(monkey.items)

monkies=parseDemMonkies(getStripedLinesFromFile('src/1211/sampleInput.data'))
processRounds(1, monkies)

print(math.modf(22/2))