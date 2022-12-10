from cpu import CPU



def addx(params):
    params[0].registers[0]+=int(params[1])



cpuinstruction={ 
    'noop':lambda x:None,
    'addx':addx
}
cpuCommands={
    'noop':[
        'noop'
    ],
    'addx':[
        'noop',
        'addx'
    ]
}



class ElfCPU(CPU):

    instructionSet=cpuinstruction
    commandsSet=cpuCommands

    def __init__(self, initRegistersWith=1):
        self.interestingSignals=[]
        super().__init__(1, ElfCPU.commandsSet, ElfCPU.instructionSet)


    def process(self, instruction: str, params: list):
        if (self.cycle - 20)%40 == 0:
            self.interestingSignals.append(self.registers[0]*self.cycle)
        super().process(instruction, params)
        

    def getInterestingSignals(self):
        return self.interestingSignals

    def getSumOfInterestingSignals(self):
        return sum(self.interestingSignals)





