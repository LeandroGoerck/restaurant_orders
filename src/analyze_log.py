from .csv_importer import CsvImporter
from .file_writer import FileWriter
from multiset import Multiset

def analyze_log(path_to_file):
    lines = CsvImporter.import_data(path_to_file)

    
    result = []
    orders_by_person= dict()
    days_ordered = dict()
    all_days = set()
    all_orders = set()
    for line in lines:
        person = line.split(",")[0]
        product = line.split(",")[1]
        day = line.split(",")[2]

        if person not in orders_by_person:
            orders_by_person[person] = Multiset()

        if person not in days_ordered:
            days_ordered[person] = Multiset()
        
        orders_by_person[person].add(product)
        days_ordered[person].add(day.split("\n")[0])

        all_orders.add(product)
        all_days.add(day.split("\n")[0])

    result.append(max(orders_by_person['maria'].distinct_elements(), key=lambda x: orders_by_person['maria'].items()))
    result.append(str(orders_by_person['arnaldo']['hamburguer']))
    result.append(all_orders - orders_by_person['joao'].distinct_elements())
    result.append(all_days - days_ordered['joao'].distinct_elements())

    FileWriter.save_data("data/mkt_campaign.txt", result)

    return print(result)
