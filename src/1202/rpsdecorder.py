from decoder import Decoder
from rpsrules import RockPaperScissorsRules


class RockPaperScissorsDecoder(Decoder):


    def __init__(self, rules=RockPaperScissorsRules()):
        self.rules=rules

    def determineOutcome(self, you: str, me: str) -> tuple:
        return self.rules.determineOutcome(you, self._mapStr2Str(you, me))


    def _mapStr2Str(self, you:str, me:str) -> str:
        return 'X' if (me == "X" and you == "B") or (me == "Y" and you == "A") or (me == "Z" and you == "C") \
          else 'Y' if (me == "X" and you == "C") or (me == "Y" and you == "B") or (me == "Z" and you == "A") \
          else 'Z'
    