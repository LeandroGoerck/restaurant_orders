import csv
from .importer import Importer

class CsvImporter(Importer):
    @staticmethod
    def import_data(arquivo):
        print(arquivo)
        if ".csv" not in str(arquivo):
            raise FileNotFoundError("Extensão inválida: '"+ arquivo + "'")

        lines = []
        try: 
            with open(arquivo) as file:
                for line in file.readlines():
                    lines.append(line)
            return lines
        except IOError:
            raise FileNotFoundError("Arquivo inexistente: '"+arquivo+"'")
