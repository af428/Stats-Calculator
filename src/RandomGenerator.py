import random
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemsFromList, randItemFromListSeed, randItemsFromListSeed


class RandomGenerator:

    def __init__(self):
        pass

    def randomNum(self, first, last):
        randomNumber.randomNum.generateRand(first, last)
        return randomNumber.randomNum.getResult()

    def randomNumSeed(self, first, last, seed):
        return randomNumberWithSeed.randomNumSeed(first, last, seed).getNum()

    def randomNumsSeed(self, first, last, n, seed):
        return randomNumbersWithSeed.randomNumsSeed(first, last, n, seed).getResult()

    def randItemFromList(self, array):
        return randItemFromList.randItemFromList(array).getItem()

    def randItemsFromList(self, n, array):
        return randItemsFromList.randItemsFromList(n, array).getItem()

    def randItemFromListSeed(self, array, seed):
        return randItemFromListSeed.randItemFromList(array, seed).getItem()

    def randItemsFromistSeed(self, n, array, seed):
        return randItemsFromListSeed.randItemsFromListSeed(n, array, seed).getItem()