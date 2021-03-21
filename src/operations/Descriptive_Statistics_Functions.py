from src.operations.addition import Addition
from src.operations.divsion import Division
from src.operations.multiplication import Multiplication
from src.operations.square import Square
from src.operations.square_root import SquareRoot
from src.operations.subtraction import Subtraction


import statistics


class StatisticsFunctions():

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



