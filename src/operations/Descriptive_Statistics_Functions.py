from src.operations.addition import Addition
from src.operations.divsion import Division
from src.operations.multiplication import Multiplication
from src.operations.square import Square
from src.operations.square_root import SquareRoot
from src.operations.subtraction import Subtraction
from src.randomOps.randomNumberWithSeed import randomNumSeed
from src.RandomGenerator import RandomGenerator
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemsFromList, randItemFromListSeed, randItemsFromListSeed

import statistics


class StatisticsFunctions:

    @staticmethod
    def mean(data):
        result = statistics.mean(data)
        return result

    @staticmethod
    def median(data):
        result = statistics.median(data)
        return result

    @staticmethod
    def mode(data):
        result = statistics.mode(data)
        return result

    @staticmethod
    def variance(data):
        result = statistics.variance(data)
        return result

    @staticmethod
    def standardDeviation(data):
        result = statistics.stdev(data)
        return result

    @staticmethod
    def z_Score(data):
        x = randomNumbersWithSeed.randNumsSeed(data)
        mean = statistics.mean(data)
        stDev = statistics.stdev(data)
        return ( x - mean) / stDev

