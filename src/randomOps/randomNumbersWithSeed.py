import random
from src.randomOps.randomNumberWithSeed import randomNumSeed


class randNumsSeed(randomNumSeed):
    def __init__(self, first, last, n, seed):
        self.first = first
        self.last = last
        self.seed = seed
        self.n = n
        self.numList = []

    def generateNumsSeed(self):
        for i in range(self.n):
            n = random.randint(self.first, self.last)
            self.numList.append(n)

    def getResult(self):
        return self.numList
