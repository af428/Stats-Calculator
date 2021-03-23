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
    # Simple Random Sampling
    def sample_list(input_list, new_list_length):
        if not input_list:
            return "Error: input list was empty"
        if new_list_length > len(input_list):
            return "Error: sample list length is bigger than original list"
        return random.sample(input_list, new_list_length)


    @staticmethod
    # Confidence Interval For a Sample
    def confidence_int_sample(confidence, sample_list):
        sample_size = len(sample_list)
        sample_mean = numpy.mean(sample_list)
        sample_std = sem(sample_list)
        degrees_freedom = sample_size - 1
        confidence_interval = t.interval(confidence, degrees_freedom, sample_std)
        return confidence_interval

    @staticmethod
    # Margin of Error
    def margin_of_error(input_list):
        return sem(input_list)

    @staticmethod
    # Cochran’s Sample Size Formula
    def cochrans(input_list):
        error = sem(input_list)
        gstd = stats.gstd(input_list)
        z = stats.szcore(input_list)
        x = (((z ** 2) * .25) / (error ** 2))
        return int(x)

    @staticmethod
    # Sample Size Given a Confidence Interval and Width
    def sample_size(input_list):
        # confidence = 0.05
        error = sem(input_list)
        std = stats.gstd(input_list)
        # z = stats.zscore(input_list)
        z = 1.96
        n = ((z * std) / error) ** 2
        return int(n)
