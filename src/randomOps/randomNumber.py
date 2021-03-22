import random


class randomNum:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.output = None
        random.seed()

    def generateRand(self):
        self.output = random.randint(self.first, self.last)

    def getResult(self):
        return self.output
