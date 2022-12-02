from game import Game
from rpsrules import RockPaperScissorsRules
from rpsdecorder import RockPaperScissorsDecoder


lines=[]

with open('src/1202/input.data', 'r') as file:
    lines=file.readlines()

game=Game(lines, RockPaperScissorsRules())


game.processGame()
print(game.getMyTotalScore())

decoderGame=Game(lines, RockPaperScissorsDecoder())
decoderGame.processGame()

print(decoderGame.getMyTotalScore())

