import unittest
from src.RandomGenerator import RandomGenerator


class RandomGeneratorTestCase(unittest.TestCase):
    def test_random_generator(self):
        random_number = RandomGenerator.get_random_number(4)
        self.assertEqual(random_number, 4)