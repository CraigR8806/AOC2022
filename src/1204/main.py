import re

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def parseAPair(line):
    m = re.findall('([0-9]+)[,-]?', line)
    return set(range(int(m[0]), int(m[1])+1)), set(range(int(m[2]), int(m[3])+1))

def isSubOrSuper(ab:tuple):
    return 1 if ab[0].issubset(ab[1]) or ab[0].issuperset(ab[1]) else 0

def doesIntersect(ab:tuple):
    return 1 if len(ab[0].intersection(ab[1])) != 0 else 0

def getTotalEncompassings(lines):
    return sum([isSubOrSuper(parseAPair(line)) for line in lines])

def getTotalIntersections(lines):
    return sum([doesIntersect(parseAPair(line)) for line in lines])




sampleLines=getStripedLinesFromFile('src/1204/sampleInput.data')
inputLines=getStripedLinesFromFile('src/1204/input.data')

print("Total number of subsets in pairs in sample data:")
print(getTotalEncompassings(sampleLines))
print()
print("Total numebr of subsets in pairs in input data:")
print(getTotalEncompassings(inputLines))
print()
print("Total number of intersections between pairs in sample data:")
print(getTotalIntersections(sampleLines))
print()
print("Total number of intersections between pairs in input data:")
print(getTotalIntersections(inputLines))

