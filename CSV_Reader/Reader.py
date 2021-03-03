
import csv
from pathlib import Path


def absolute_path(filepath):
    relative = Path(filepath)
    return relative.absolute()


class Reader:
    content = []

    def __init__(self, file):
        self.content = []
        self.reader(file)

    def reader(self, path):
        with open(absolute_path(path)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_line = csv_file.readline()
            for row in csv_reader:
                if '' in row:
                    row.remove('')
                self.content.append(row)