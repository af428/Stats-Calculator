from src.operations.addition import Addition
from src.operations.divsion import Division
from src.operations.multiplication import Multiplication
from src.operations.square import Square
from src.operations.square_root import SquareRoot
from src.operations.subtraction import Subtraction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = Addition.addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = Subtraction.subtraction(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = Multiplication.multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = round(Division.division(x, y), 9)
        return self.result

    def square(self, x):
        self.result = Square.square(x)
        return self.result

    def square_root(self, x):
        self.result = SquareRoot.square_root(x)
        return self.result
