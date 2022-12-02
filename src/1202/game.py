from rules import Rules
from round import Round


class Game:



    def __init__(self, moveData:list, rules:Rules):
        self.moveData = moveData
        self.rules = rules
        self.myTotalScore = 0
        self.yourTotalScore = 0
        self.rounds = []


    def processGame(self):
        for move in self.moveData:
            yourScore, myScore = self.rules.determineOutcome(move[0], move[2])
            self.rounds.append(Round(yourScore, myScore))
        
        self.myTotalScore = sum(list(map(lambda x:x.getMyScore(), self.rounds)))
        self.yourTotalScore = sum(list(map(lambda x:x.getYourScore(), self.rounds)))


    def getMyTotalScore(self):
        return self.myTotalScore

    def getYourTotalScore(self):
        return self.yourTotalScore