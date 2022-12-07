from fso import FSO
from dir import Dir
from file import File
import re

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def moveCursor(cmd:str, cursor:list) -> Dir:
    if cmd == "..":
        cursor.pop(-1)
    elif cmd == "/":
        cursor=cursor[0:1]
    else:
        landingDir=cursor[-1].getChild(cmd)
        if landingDir == None:
            print("Directory doesn't appear to exist")
            exit(1)
        cursor.append(landingDir)


def parseAndBuildFSO(lines:list):
    root=Dir("/")
    cursor=[root]
    allDirs=[]
    
    for line in lines:
        cmdM = re.findall("^\$ (cd|ls) ?([a-zA-Z0-9\./]*)", line)
        dataM = re.findall("^(dir|[0-9]+) ([a-zA-Z0-9\.]+)", line)

        if len(cmdM) > 0:
            if cmdM[0][0] == "cd":
                moveCursor(cmdM[0][1], cursor)
        if len(dataM) > 0:
            cursor[-1].addFSO(Dir(dataM[0][1]) if dataM[0][0] == "dir" else File(dataM[0][1], dataM[0][0]))
            if dataM[0][0] == "dir":
                allDirs.append(cursor[-1].fsos[-1])

    return root, allDirs

def getAllDirsBelowOrOfSize(dirs:list, size:int, recursive=True):
    return list(filter(lambda x:x.getSize(recursive) <= size, dirs))

def getAllDirsAboveOrOfSize(dirs:list, size:int, recursive=True):
    return list(filter(lambda x:x.getSize(recursive) >= size, dirs))

def getSumOfSizes(dirs:list, recursive=True):
    return sum(map(lambda x:x.getSize(recursive), dirs))

def getSumOfSizesOfFilteredDirs(dirs:list, size:int, recursive=True):
    return getSumOfSizes(getAllDirsBelowOrOfSize(dirs, size, recursive), recursive)

def getRequiredSpaceForUpdate(root:Dir, updateSize:int, totalDiskSize:int):
    return updateSize - (totalDiskSize - root.getSize())

def findDirectoryToDelete(root:dir, dirs:list, updateSize:int, totalDiskSize:int):
    return sorted(getAllDirsAboveOrOfSize(dirs, getRequiredSpaceForUpdate(root, updateSize, totalDiskSize)), key=lambda x:x.getSize())[0].getSize()



rootSample, sampleAllDirs = parseAndBuildFSO(getStripedLinesFromFile('src/1207/sampleInput.data'))
root, allDirs = parseAndBuildFSO(getStripedLinesFromFile('src/1207/input.data'))

print(getSumOfSizesOfFilteredDirs(sampleAllDirs, 100000))
print(getSumOfSizesOfFilteredDirs(allDirs, 100000))

sampleAllDirs.append(rootSample)
allDirs.append(root)
print(findDirectoryToDelete(rootSample, sampleAllDirs, 30000000, 70000000))
print(findDirectoryToDelete(root, allDirs, 30000000, 70000000))