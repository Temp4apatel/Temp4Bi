import csv

class MastDataReader:
    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def get_all(self):
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            return list(csvReader)
   
    def top(self, n):
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            sortedList = list(sorted(csvReader, key=lambda row: float(row[10]), reverse=False))
            return sortedList[0:n]

    def list_filtered(self, filter_expr):
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            filteredList = list(filter(filter_expr, csvReader))
            return filteredList
