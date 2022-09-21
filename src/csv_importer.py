import csv
from .importer import Importer

class CsvImporter(Importer):
    @staticmethod
    def import_data(arquivo):
        if ".csv" not in arquivo:
            raise ValueError("Extensão inválida: '"+ arquivo + "'")
        lines = []
        with open(arquivo) as file:
            for line in file.readlines():
                lines.append(line)

        return lines
