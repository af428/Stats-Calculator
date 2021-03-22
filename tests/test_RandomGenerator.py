import unittest
from src.RandomGenerator import RandomGenerator


class RandomGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.Randomizer = RandomGenerator()
        print('')
        print('setUp')


if __name__ == '__main__':
    unittest.main()