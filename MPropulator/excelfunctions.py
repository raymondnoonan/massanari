import csv
import openpyxl
import helpers


class Table:

    def __init__(self, path):
        self.path = path
        self.length = None

    def __iter__(self):
        self.length = 0

        with open(self.path, 'rU') as data:
            reader = csv.DictReader(data)
            for row in reader:
                self.length += 1
                yield row

    def __len__(self):
        if self.length is None:
            for row in self:
                continue
        return self.length