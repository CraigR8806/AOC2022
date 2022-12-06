
def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out


def findMarker(data, kernelLength):
    kernelStart=0
    for kernelStart in range(len(data)):
        if len(set(data[kernelStart:kernelStart+kernelLength])) == kernelLength:
            break
    
    return kernelStart+kernelLength

print("Sample Input output part 1:")
[print(findMarker(line, 4)) for line in getStripedLinesFromFile('src/1206/sampleInput.data')]
print("Input output part 1:")
[print(findMarker(line, 4)) for line in getStripedLinesFromFile('src/1206/input.data')]

print("Sample Input output part 2:")
[print(findMarker(line, 14)) for line in getStripedLinesFromFile('src/1206/sampleInput.data')]
print("Input output part 2:")
[print(findMarker(line, 14)) for line in getStripedLinesFromFile('src/1206/input.data')]