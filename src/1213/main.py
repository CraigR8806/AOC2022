from functools import cmp_to_key
from random import sample
import re
from copy import deepcopy

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out


def parsePacketPairs(lines):
    packetInfo={}
    packetPairs=[]
    for line in lines:
        if line:
            if 'left' not in packetInfo.keys():
                packetInfo['left']=eval(line)
            else:
                packetInfo['right']=eval(line)
                packetPairs.append(deepcopy(packetInfo))
                packetInfo.clear()

    return packetPairs

            
def compare(a, b):
    if isinstance(a, list) and not isinstance(b, list):
        return compare(a, [b])
    if isinstance(b, list) and not isinstance(a, list):
        return compare([a], b)
    if isinstance(b, list) and isinstance(a, list):
        index=0
        if len(a) <= index or len(b) <= index:
            if len(a) <= index:
                return 1
            return -1
        res=compare(a[index], b[index])
        while res==0:
            index+=1
            if len(a) <= index or len(b) <= index:
                if len(a) == len(b):
                    res=0
                    break
                if len(a) <= index:
                    res = 1
                    break
                res=-1
                break
            res=compare(a[index], b[index])
        return res

    return -1 if a > b else 1 if b > a else 0


def findProperPackets(packetPairs):
    correct=[]
    for i, pair in enumerate(packetPairs):
        res=compare(pair['left'], pair['right'])
        if res == 1:
            correct.append(i+1)
        
    return sum(correct)

def findDecoderKey(packetPairs):
    allPackets=[]
    for pair in packetPairs:
        allPackets.append(pair['left'])
        allPackets.append(pair['right'])
    
    allPackets.append([[2]])
    allPackets.append([[6]])
    allPacketsSorted=sorted(allPackets, key=cmp_to_key(compare), reverse=True)

    [print(packet) for packet in allPacketsSorted]

    return (allPacketsSorted.index([[2]])+1) * (allPacketsSorted.index([[6]])+1)

samplePair=parsePacketPairs(getStripedLinesFromFile('AOC2022/src/1213/sampleInput.data'))
pair=parsePacketPairs(getStripedLinesFromFile('AOC2022/src/1213/input.data'))

print(findDecoderKey(samplePair))
print(findDecoderKey(pair))