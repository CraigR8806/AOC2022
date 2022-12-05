import re
from move import Move

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def parseInput(lines:list):
    lines.reverse()
    moveList=[]
    stacks=[]
    for line in lines:
        moveData=[int(match[2])-1 for match in re.findall("((move| from| to) ([0-9]+))", line)]
        if len(moveData)>0:
            moveList.append(Move(moveData[0]+1, moveData[1], moveData[2]))
        
        stackCountData=re.findall("([0-9]+)( {3}| $)", line)
        if len(stackCountData)>0:
            stackCount=int(stackCountData[-1][0])
            for stack in range(stackCount):
                stacks.append([])
        
        stackData=[match[1] for match in re.findall("(\[[A-Z]\]| {2,5})", line)]
        if len(re.findall('[A-Z]', str.join('', stackData)))>0:
            for stack,data in zip(stacks,stackData):
                if data != " ":
                    stack.append(data)

    moveList.reverse()
    return moveList,stacks


def executeMove(stacks, move:Move):
    pulled=stacks[move.getFrom()][-move.getNumberToMove():]
    pulled.reverse()
    stacks[move.getTo()].extend(pulled)
    stacks[move.getFrom()]=stacks[move.getFrom()][:-move.getNumberToMove()]

def readTheTop(stacks):
    return "".join([stack[-1] if len(stack)>0 else " " for stack in stacks])


sampleInputLines=getStripedLinesFromFile('src/1205/sampleInput.data')
inputLines=getStripedLinesFromFile('src/1205/input.data')


moveList, stacks=parseInput(sampleInputLines)
for move in moveList:
    executeMove(stacks, move)

print(readTheTop(stacks))

moveList, stacks=parseInput(inputLines)
for move in moveList:
    executeMove(stacks, move)

print(readTheTop(stacks))




