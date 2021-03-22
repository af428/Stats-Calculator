from src.randomOps.randItemFromList import randItemFromList


class randItemsFromList(randItemFromList):
    def __init__(self, array, n):
        self.array = array
        self.genItems = []
        self.n = n
        self.generateChoices()

    def generateChoices(self):
        if self.n <= len(self.array):
            for i in range(self.n):
                super().genItem()
                self.genItems.append(super().getItem())
                self.array.remove(super().getItem())
        else:
            self.genItems = "ERROR: n is larger than array size"

    def getItems(self):
        return self.genItems