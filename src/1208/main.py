from functools import reduce
import re

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def parseTreeMDA(lines):
    return [list(map(lambda x:int(x), re.findall("([0-9])", line))) for line in lines]
        
def above(mda, y, x):
    return [] if y == 0 else [subMDA[x] for subMDA in mda[:y]]

def below(mda, y, x):
    return [] if y == len(mda) else [subMDA[x] for subMDA in mda[y+1:]]

def left(mda, y, x):
    return [] if x == 0 else mda[y][:x]

def right(mda, y, x):
    return [] if x == len(mda[y]) else mda[y][x+1:]

def treeIsHidden(mda, y, x):
    directions=[above(mda, y, x), below(mda, y, x), left(mda, y, x), right(mda, y, x)]
    return all([len([t for t in direction if t>=mda[y][x]])>0 for direction in directions])

def indexOf(l, v):
    try:
        return l.index(v)
    except:
        return -1

def modiIndexOf(l, v):
    i=indexOf(l, v)
    return len(l)-1 if i == -1 else i

def getScenicScore(mda, y, x):
    directions=[list(reversed(above(mda, y, x))), below(mda, y, x), list(reversed(left(mda, y, x))), right(mda, y, x)]
    return reduce(lambda a,b:a*b, [modiIndexOf(list(map(lambda c:c<mda[y][x], direction)), False)+1 for direction in directions])

def numberOfVisibleTrees(mda):
    visible=0
    for y in range(len(mda)):
        for x in range(len(mda[y])):
            visible+=0 if treeIsHidden(mda, y, x) else 1

    return visible

def calculateHighestScenicScore(mda):
    max=0
    for y in range(len(mda)):
        for x in range(len(mda[y])):
            scenicScore=getScenicScore(mda, y, x)
            if scenicScore > max:
                max = scenicScore
    return max




sampleTrees=parseTreeMDA(getStripedLinesFromFile("src/1208/sampleInput.data"))
trees=parseTreeMDA(getStripedLinesFromFile("src/1208/input.data"))

print(numberOfVisibleTrees(sampleTrees))
print(numberOfVisibleTrees(trees))

print(calculateHighestScenicScore(sampleTrees))
print(calculateHighestScenicScore(trees))


