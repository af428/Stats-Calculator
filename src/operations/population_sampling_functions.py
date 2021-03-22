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
        error = sem(input_list)
        gstd = stats.gstd(input_list)
        z = stats.szcore(input_list)
        x = (((z ** 2) * .25) / (error ** 2))
        return int(x)

    @staticmethod
    def confidence_int_sample(confidence, sample_list):
        x = len(sample_list)
        average = numpy.mean(sample_list)
        std_error_mean = sem(sample_list)
        interval = std_error_mean * t.ppf((1 +confidence)/2, x - 1)
        high = average + interval
        low = average - interval
        return high, low

    @staticmethod
    def margin_of_error(input_list):
        return sem(input_list)


