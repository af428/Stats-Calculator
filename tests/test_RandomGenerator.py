import unittest
from src.RandomGenerator import RandomGenerator


class RandomGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.Randomizer = RandomGenerator()
        print('')
        print('setUp')

    def test_random_number(self):
        print("- Random Number Generator Test -")
        print("Random Number: ")
        print(self.Randomizer.randomNum(0, 25))


if __name__ == '__main__':
    unittest.main()
