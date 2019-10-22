import csv

class MastDataReader:
    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def get_all(self):
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            return list(csvReader)
   
    def sorted_top(self, n):
        current_rent_column_index = 10 
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            sortedList = list(sorted(csvReader, key=lambda row: float(row[current_rent_column_index]), reverse=False))
            return sortedList[0:n]

    # filter_expr: filter lamda expression.
    def list_filtered(self, filter_expr):
        with open(self.path_to_csv, newline='') as fd:
            csvReader = csv.reader(fd, delimiter = ',')
            next(csvReader)
            filteredList = list(filter(filter_expr, csvReader))
            return filteredList
