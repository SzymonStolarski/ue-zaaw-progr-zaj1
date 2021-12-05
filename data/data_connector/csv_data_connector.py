import csv


class CSVDataConnector:
    def __init__(self, path) -> None:
        self.path = path

    def load_data(self):
        with open(self.path, 'r', encoding="utf8") as csv_file:
            return list(csv.DictReader(csv_file))
