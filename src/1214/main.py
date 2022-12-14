import re
import math

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out



def parseMap(lines, accountForFloor=False):
    allCoords=[]
    for line in lines:
        parsedCoords=re.findall("([0-9]+)+", line)
        coords=[[int(parsedCoords[i+1]), int(parsedCoords[i])] for i in range(0,len(parsedCoords),2)]
        allCoords.append(coords)

    mn, mx = findMinMaxXY(allCoords)
    

    if accountForFloor:
        h=mx[0]+2
        floorHalfW=math.ceil(h/math.tan(math.radians(60)))+100
        allCoords.append([[mx[0]+2, 500-floorHalfW], [mx[0]+2, 500+floorHalfW]])
        mn, mx = findMinMaxXY(allCoords)

    sandSrc=(0, 500 - mn[1])
    
    normalCoords = normalizeCoords(allCoords, mn, mx)
    mn, mx = findMinMaxXY(normalCoords)
    
    map=[]
    for j in range(mx[0]+1):
        map.append([])
        for i in range(mx[1]+1):
            map[j].append(".")

    for i in range(len(normalCoords)):
        for j in range(len(normalCoords[i])-1):
            startX = min([normalCoords[i][j][1], normalCoords[i][j+1][1]])
            endX = max([normalCoords[i][j][1], normalCoords[i][j+1][1]])
            startY = min([normalCoords[i][j][0], normalCoords[i][j+1][0]])
            endY = max([normalCoords[i][j][0], normalCoords[i][j+1][0]])
            if endX - startX == 0:
                for py in range(startY, endY+1):
                    map[py][startX] = "#"
            if endY - startY == 0:
                for px in range(startX, endX+1):
                    map[startY][px] = "#"
                    
    
    return map,sandSrc
            
def showMap(map):
    return "\n".join(["".join(line) for line in map])



def normalizeCoords(coords, min:tuple, max:tuple):
    xF=min[1]
    coords=[[[coords[i][j][0], coords[i][j][1] - xF] for j in range(len(coords[i])) ] for i in range(len(coords))]
    return coords
    
def flatten(v, out=None):
    if out is None:
        out=[]
    if v is None:
        return
    if isinstance(v, list):
        index=0
        vs=[]
        while len(v) > index:
            flatten(v[index], out)
            index+=1
        return out
    if isinstance(v, int):
        out.append(v)
    
            
def findMinMaxXY(coords):
    flatX = flatten([[coords[i][j][1] for j in range(len(coords[i])) ] for i in range(len(coords))])
    flatY = flatten([[coords[i][j][0] for j in range(len(coords[i])) ] for i in range(len(coords))])

    minX=min(flatX)
    minY=min(flatY)
    maxX=max(flatX)
    maxY=max(flatY)

    return (minY, minX), (maxY, maxX)


def letTheSandFallWhereItMay(map:list, sandSrc:tuple):
    sandIsBuilding=True
    currentSandPosition=sandSrc
    unitsOfSand=0
    while sandIsBuilding:
        below=None
        belowL=None
        belowR=None
        try:
            below=map[currentSandPosition[0]+1][currentSandPosition[1]]
            belowL=map[currentSandPosition[0]+1][currentSandPosition[1]-1]
            belowR=map[currentSandPosition[0]+1][currentSandPosition[1]+1]
        except:
            break
        if below == ".":
            currentSandPosition=(currentSandPosition[0]+1,currentSandPosition[1])
            continue
        if below == "#" or below == "O":
            if belowL == "#" or belowL == "O":
                if belowR == "#" or belowR == "O":
                    map[currentSandPosition[0]][currentSandPosition[1]] = "O"
                    # print(showMap(map))
                    # print()
                    unitsOfSand+=1
                    if currentSandPosition == sandSrc:
                        break
                    currentSandPosition=sandSrc
                    
                else:
                    currentSandPosition=(currentSandPosition[0]+1,currentSandPosition[1]+1)
            else:
                currentSandPosition=(currentSandPosition[0]+1,currentSandPosition[1]-1)
    return unitsOfSand
        


sampleLines=getStripedLinesFromFile('src/1214/sampleInput.data')
lines=getStripedLinesFromFile('src/1214/input.data')
sMap,ssandSrc=parseMap(sampleLines)
map,sandSrc=parseMap(lines)

print(letTheSandFallWhereItMay(sMap, ssandSrc))
print(letTheSandFallWhereItMay(map, sandSrc))

s2Map,s2sandSrc=parseMap(sampleLines, True)
map,sandSrc=parseMap(lines, True)

print(letTheSandFallWhereItMay(s2Map, s2sandSrc))
print(letTheSandFallWhereItMay(map, sandSrc))


