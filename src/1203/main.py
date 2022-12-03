import math
import re

sampleLines=[]
inputLines=[]
with open('src/1203/sampleInput.data', 'r') as file:
    sampleLines=[line.strip('\n') for line in file.readlines()]

with open('src/1203/input.data', 'r') as file:
    inputLines=[line.strip('\n') for line in file.readlines()]

def findMatchesBetween2Lines(lines):
    return set([c for c in lines[0] if re.search(c, lines[1])])
    

def splitAndFindMatches(line):
    return findMatchesBetween2Lines([line[:int(len(line)/2)], line[int(len(line)/2):]])


def mapIt(a): #Flip it, scoot it, compress it, flip it
    out=-ord(a) + 96
    return -out+58 if out > 0 else abs(out)

def findBadge(elves):#Just search first elf for all items, find any matches between elf 1 and 2, then only iter over matches
    matches1and2=findMatchesBetween2Lines([elves[0], elves[1]])
    thebadge=None
    for c in matches1and2:
        if re.search(c, elves[2]):
            thebadge=c
            break
    return c


def getThatTotal(input:list):
    return sum([sum([mapIt(y) for y in x]) for x in input])

sampleTotalMatches=[splitAndFindMatches(line) for line in sampleLines]
inputTotalMatches=[splitAndFindMatches(line) for line in inputLines]
sampleTotalBadges=[findBadge(sampleLines[x:x+3]) for x in range(0, len(sampleLines), 3)]
inputTotalBadges=[findBadge(inputLines[x:x+3]) for x in range(0, len(inputLines), 3)]





print("Puzzle Sample Input Total:")
print(getThatTotal(sampleTotalMatches))
print()
print("My Sample Input Total:")
print(getThatTotal(inputTotalMatches))
print()
print("Puzzle Sample Input Badge Total:")
print(getThatTotal(sampleTotalBadges))
print()
print("My Sample Input Badge Total:")
print(getThatTotal(inputTotalBadges))