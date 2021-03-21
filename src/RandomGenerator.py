import random
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemFromListSeed, randItemsFromList, randItemsFromListSeed

class RandomGenerator:

    def __init__(self):
        pass

    def randomNum(self, start, end):
        return randomNumber.randomNum(start, end).getResult()