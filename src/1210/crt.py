



class CRT:


    def __init__(self, width:int, height:int, pixelWidth:int):
        self.width = width
        self.height = height
        self.pixelWidth = pixelWidth
        self.screen = [[]]
        self.currentRow=0

    def draw(self, cycle:int, x:int):
        if cycle >= self.height*self.width:
            return
        if cycle%self.width == 0:
            self.screen.append([])
            self.currentRow+=1

        pixel=[int(x+(i+1-self.pixelWidth/2)) for i in range(self.pixelWidth)]
        self.screen[self.currentRow].append("#" if cycle%self.width in pixel else ".")

    def __str__(self):
        return "\n".join(["".join(line) for line in self.screen])

        
    