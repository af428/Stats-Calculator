import statistics
import random
import math
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
        conf = sample_std * t.ppf((1 + confidence) / 2., sample_size-1)
        return sample_mean-conf, sample_mean, sample_mean+conf

    @staticmethod
    # Margin of Error
    def margin_of_error(input_list, significance_level):
        sample_size = len(input_list)
        z_score = scipy.stats.norm.ppf(significance_level)
        std = sem(sample_list)
        margin_error = z_score * (std/math.sqrt(sample_size))
        return margin_error

    @staticmethod
    # Cochran’s Sample Size Formula
    def cochran(input_list):
        error = sem(input_list)
        gstd = spicy.stats.gstd(input_list)
        z = stats.szcore(input_list)
        x = (((z ** 2) * .25) / (error ** 2))
        return int(x)

    @staticmethod
    # Sample Size Given a Confidence Interval and Width
    def sample_size(input_list):
        error = sem(input_list)
        std = stats.gstd(input_list)
        z = stats.zscore(input_list)
        n = ((z * std) / error) ** 2
        return int(n)
