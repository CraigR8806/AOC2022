import re
from sensor import Sensor

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out



def normalizeSensors(sensors:list, delta:tuple):
    for sensor in sensors:
        sensor.modifyPosition(delta)
        sensor.modifyBeaconPosition(delta)
    
    
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
    flatX = [coords[i][1] for i in range(len(coords))]
    flatY = [coords[i][0] for i in range(len(coords))]

    minX=min(flatX)
    minY=min(flatY)
    maxX=max(flatX)
    maxY=max(flatY)

    return (minY, minX), (maxY, maxX)

def showMap(map):
    return "\n".join(["".join(line) for line in map])

def getOuterPoint(center, yLevel, dist, start):
    return (yLevel, (-1 if start else 1)*abs(center[0] - yLevel) + center[1] - dist)





# print(showMap(map))


def parseSensors(lines):
    sensors=[]
    sensorPoss=[]
    sensorRanges=[]
    cbPoss=[]
    for line in lines:
        posM=re.findall("([0-9]+)", line)
        pos=(int(posM[1]), int(posM[0]))
        cbPos=(int(posM[3]), int(posM[2]))
        sensor = Sensor(pos,cbPos)
        
        sensors.append(sensor)
        sensorPoss.append(pos)
        sensorRanges.extend([(pos[1]+(sensor.getManahattanDistance()*(-1 if i%2==0 else 1)*(0 if i<=1 else 1)), pos[1]+(sensor.getManahattanDistance()*(-1 if i%2==1 else 1)*(0 if i>1 else 1))) for i in range(4)])
        cbPoss.append(cbPos)

    mn, mx = findMinMaxXY(sensorRanges)
    delta=(mn[0]*-1, mn[0]*-1)
    return sensors, delta, mn, mx


def visualize(sensors, delta, mn, mx):
    mx=(mx[0]+delta[0], mx[1]+delta[1])
    normalizeSensors(sensors, delta)
    map=[]
    for i in range(mx[0]+1):
        map.append([])
        for j in range(mx[1]+1):
            map[i].append(".")

    for sensor in sSensors:
        c=sensor.getPosition()
        d=sensor.getManahattanDistance()
        for y in range(c[0]-d, c[0]+d+1):
            sx=getOuterPoint(c, y, d, True)[1]
            ex=getOuterPoint(c, y, -d, False)[1]
            for ax in range(sx, ex+1):
                map[y][ax] = "#"

    for sensor in sSensors:
        c=sensor.getPosition()
        b=sensor.getClosestBeaconPosition()
        map[c[0]][c[1]]="S"
        map[b[0]][b[1]]="B"

    print(showMap(map))

def getNumberOfSpotsBeaconsCannotBeOnLine(sensors:list, mn:tuple, mx:tuple, line:int):


    noBeaconPoints=set()
   
    for sensor in sensors:
        pos=sensor.getPosition()
        dist=sensor.getManahattanDistance()
        startY=pos[0] - dist - 1
        endY=pos[0] + dist + 1
        if line >= startY and line <= endY:
            startX=getOuterPoint(pos, line, dist, True)[1] - 1
            endX=getOuterPoint(pos, line, dist, False)[1] + 1
            for x in range(mn[1], mx[1]):
                if x >= startX and x <= endX:
                    noBeaconPoints.add((line, x))

    return len(noBeaconPoints)





# sSensors,sDelta,smn,smx = parseSensors(getStripedLinesFromFile('src/1215/sampleInput.data'))
# sensors,delta,mn,mx = parseSensors(getStripedLinesFromFile('src/1215/input.data'))

sSensors,sDelta,smn,smx = parseSensors(getStripedLinesFromFile('AOC2022/src/1215/sampleInput.data'))
sensors,delta,mn,mx = parseSensors(getStripedLinesFromFile('AOC2022/src/1215/input.data'))

print(getNumberOfSpotsBeaconsCannotBeOnLine(sSensors, smn, smx, 10))
print(getNumberOfSpotsBeaconsCannotBeOnLine(sensors, mn, mx, 2000000))


