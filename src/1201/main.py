from elf import Elf

def addElf(es, i, e):
    es.append(Elf(i, e))
    e.clear()

def sumOfTopX(l:list, x:int):
    return sum(l[:x])


elves=[]
with open("src/1201/input.data", "r") as file:
    lines = file.readlines()
    entries=[]
    index=0
    for line in lines:
        line=line.strip("\n")
        if  line == "" :
            addElf(elves, index, entries)
            index+=1
        else:
            entries.append(int(line))
    
    addElf(elves, index, entries)


es = sorted(elves, key=lambda x:x.getTotalCals(), reverse=True)

print("The most calories held by one elf: " + str(es[0].getTotalCals()))

print("The total calories held by the top 3 elves: " + str(sumOfTopX(list(map(lambda x:x.getTotalCals(), es)), 3)))

    
