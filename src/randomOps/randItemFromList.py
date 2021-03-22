import random


class randItemFromList:
    def __init__(self, array):
        self.array = array
        random.seed()
        self.genItem()
        self.output = None

    def genItem(self):
        if not isinstance(self.array, list):
            self.output = "ERROR: Input is not an Array"
        else:
            self.output = random.choice(self.array)

    def getItem(self):
        return self.output