import unittest

from src.calculator.calculator import Calculator
from CSV_Reader.Reader import Reader


class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        file = Reader("tests/data/Unit_Test_Addition.csv").content
        print("TESTING ADDITION\n")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} +  {1:4} =  {2:4}'.format(row[0], row[1], row[2]))
            self.assertEqual(self.calculator.add(row[0], row[1]), float(row[2]))
            self.assertEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.add(5, 6), 11)

    def test_subtraction(self):
        file = Reader("tests/data/Unit_Test_Subtraction.csv").content
        print("TESTING SUBTRACTION\n")
        for row in file:
            # print('---->: {0:4} -  {1:4} =  {2:4}'.format(row[1], row[0], row[2]))
            self.assertEqual(self.calculator.subtract(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.subtract(5, 6), 1)

    def test_multiplication(self):
        file = Reader("tests/data/Unit_Test_Multiplication.csv").content
        print("TESTING MULTIPLICATION\n")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} x  {1:4} =  {2:4}'.format(row[0], row[1], row[2]))
            self.assertEqual(self.calculator.multiply(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.multiply(5, 6), 30)

    def test_division(self):
        file = Reader("tests/data/Unit_Test_Division.csv").content
        print("TESTING DIVISION\n")
        for row in file:
            result = float(row[2])
            # print('---->: {0:4} / {1:4} =  {2:4}'.format(row[1], row[0], row[2]))
            self.assertEqual(self.calculator.divide(row[0], row[1]), float(row[2]))
            # self.assertEqual(self.calculator.divide(6, 30), 5)

    def test_square(self):
        file = Reader("tests/data/Unit_Test_Square.csv").content
        print("TESTING SQUARE\n")
        for row in file:
            result = float(row[1])
            # print('---->: {0:4} ^ {1:2} =  {2:4}'.format(row[0], 2, row[1]))
            self.assertEqual(self.calculator.square(row[0]), float(row[1]))
            self.assertEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.square(5), 25)

    def test_square_root(self):
        file = Reader("tests/data/Unit_Test_Square_Root.csv").content
        print("TESTING SQUARE ROOT\n")
        for row in file:
            result = float(row[1])
            # print('---->: Square Root of {0:4} =  {1:4}'.format(row[0], row[1]))
            self.assertAlmostEqual(self.calculator.square_root(row[0]), float(row[1]))
            self.assertAlmostEqual(self.calculator.result, result)
            # self.assertEqual(self.calculator.square_root(100), 10)
