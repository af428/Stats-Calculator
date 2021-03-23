import random
from src.randomOps.randomNumber import randomNum


class randomNumSeed(randomNum):
    def __init__(self, first, last, seed):
        self.first = first
        self.last = last
        random.seed(seed)
        self.output = random.randint(self.first, self.last)

    def getNum(self):
        return self.output
