import statistics
import random
from src.operations.Descriptive_Statistics_Functions import StatisticsFunctions
from src.randomOps.randomNumberWithSeed import randomNumSeed
from src.RandomGenerator import RandomGenerator
from src.randomOps import randomNumber, randomNumberWithSeed, randomNumbersWithSeed, randItemFromList, randItemsFromList, randItemFromListSeed, randItemsFromListS
from scipy import stats
from scipy.stats import sem, t

class PopulationSamplingFunctions:
    @staticmethod
    def cochrans (input_list):