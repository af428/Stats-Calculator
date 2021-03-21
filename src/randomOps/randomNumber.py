import random


class randomNum:
    def __init__(self, first, last):
        random.seed()
        self.first = first
        self.last = last
        self.output = None

    def generateRand(self):
        self.output = random.randint(self.first, self.last)

    def getResult(self):
        return self.output
