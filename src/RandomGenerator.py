import random
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemsFromList, randItemFromListSeed, randItemsFromListSeed


class RandomGenerator:

    def randomNum(self, first, last):
        return randomNumber.randomNum(first, last).getResult()

    def randomNumSeed(self, first, last, seed):
        return randomNumberWithSeed.randomNumSeed(first, last, seed).getResult()

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