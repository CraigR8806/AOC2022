from rules import Rules
from abc import ABC, abstractmethod


class Decoder(Rules, ABC):

    def __init__(self):
        pass

    @abstractmethod
    def determineOutcome(self, you: str, me: str) -> tuple:
        pass