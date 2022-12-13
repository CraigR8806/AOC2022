from terrain import Terrain
import re


def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def convertCharToHeight(char):
    return -2 if char == "E" else -1 if char == "S" else ord(char)-97

def parseTerrain(lines):
    return Terrain([list(map(lambda x:convertCharToHeight(x), re.findall("([a-zSE])", line))) for line in lines])


    



# sampleTerrain=parseTerrain(getStripedLinesFromFile('AOC2022/src/1212/sampleInput.data'))
# sampleTerrain=parseTerrain(getStripedLinesFromFile('src/1212/sampleInput.data'))
# terrain=parseTerrain(getStripedLinesFromFile('src/1212/input.data'))
terrain=parseTerrain(getStripedLinesFromFile('AOC2022/src/1212/input.data'))


# print(sampleTerrain.findShortestPath())
print(terrain.findShortestPath())
