import random
from src.randomOps.randItemsFromList import randItemsFromList


class randItemsFromListSeed(randItemsFromList):
    def __init__(self, array, n, seed):
        super().__init__(array, n)
        self.seed = seed
        random.seed(self.seed)
        super().genItem()
