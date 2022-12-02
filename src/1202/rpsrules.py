from rules import Rules
import math
import re


class RockPaperScissorsRules(Rules):

    def determineOutcome(self, you: str, me: str) -> tuple:
        
        result=math.tan(self._mapStr2Number(you) - self._mapStr2Number(me))
        basePointsMe = 6 if result < 0 else 0 if result > 0 else 3
        basePointsYou = 6 - basePointsMe

        pointsMe=self._mapStr2Number(me) + basePointsMe
        pointsYou=self._mapStr2Number(you) + basePointsYou

        return (pointsYou, pointsMe)



    def _mapStr2Number(self, x:str)->str:
        return 1 if re.match("(A|X)", x) else 2 if re.match("(B|Y)", x) else 3



