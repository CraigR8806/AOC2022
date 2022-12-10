from abc import ABC



class CPU(ABC):

    def __init__(self, numberOfRegisters:int, commands:dict,  instructionSet:dict, initRegistersWith=1):
        self.instructionSet = instructionSet
        self.registers=[initRegistersWith for i in range(numberOfRegisters)]
        self.cycle=1
        self.commands=commands


    def process(self, instruction:str, params:list):
        self.cycle+=1
        params.insert(0, self)
        self.instructionSet[instruction](params)
        

    def compile(self, command) -> list:
        return self.commands[command]

    def getCycle(self)->int:
        return self.cycle-1

    def getValueInRegister(self, reg:int)->int:
        return self.registers[reg]