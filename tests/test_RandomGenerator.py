import unittest
from src.RandomGenerator import RandomGenerator


class RandomGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.Randomizer = RandomGenerator()
        print('')
        print('Random Generator Successfully Initialized')
        print('')

    def test_random_number(self):
        print("- Random Number Generator Test -")
        print("Random Number: ")
        print(self.Randomizer.randomNum(0, 25))

    def test_random_number_by_seed_float(self):
        print("- Random Number Using Seed Test -")
        seed = 5
        first = 0
        last = 25
        print("Seed Used for Randoms: ", seed)
        value1 = self.Randomizer.randomNumSeed(first, last, seed)
        value2 = self.Randomizer.randomNumSeed(first, last, seed)
        self.assertEqual(value1, value2)
        print(value1, value2)


if __name__ == '__main__':
    unittest.main()
