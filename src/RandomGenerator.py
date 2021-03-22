import random
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemFromListSeed, randItemsFromList, randItemsFromListSeed


class RandomGenerator:

    def __init__(self):
        pass

    def randomNum(self, first, last):
        return randomNumber.randomNum(first, last).getResult()

    def randomNumSeed(self, first, last, seed):
        return randomNumberWithSeed.randomNumSeed(first, last, seed).getResult()

    def randomNumsSeed(self, first, last, n, seed):
        return randomNumberWithSeed.randomNumSeed(first, last, seed).getResult()