from elfcpu import ElfCPU
from cpu import CPU
from crt import CRT
import re


def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out



def parseAndExec(lines:list, cpu:CPU, crt:CRT):
    for line in lines:
        commandAndParams=re.findall("([a-zA-Z]+|-?[0-9]+) ?", line)
        for instruction in cpu.compile(commandAndParams[0]):
            crt.draw(cpu.getCycle(), cpu.getValueInRegister(0))
            cpu.process(instruction, commandAndParams[1:])
            
        


sampleCPU=ElfCPU()
sampleCRT=CRT(40, 6, 3)
cpu=ElfCPU()
crt=CRT(40, 6, 3)

parseAndExec(getStripedLinesFromFile('src/1210/sampleInput.data'), sampleCPU, sampleCRT)
parseAndExec(getStripedLinesFromFile('src/1210/input.data'), cpu, crt)

print(sampleCPU.getSumOfInterestingSignals())
print(cpu.getSumOfInterestingSignals())


print(sampleCRT)
print(crt)
