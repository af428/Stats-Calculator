import random
from src.randomOps.randItemFromList import randItemFromList


class randItemsFromList(randItemFromList):
    def __init__(self, array, seed):
        super().__init__(array)
        self.genItems = []
        random.seed(seed)
        super().genItem()
