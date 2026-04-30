import csv
import json

#temperatura de referinta
MAX_TEMP = 80
#tensiunea de referinta
MIN_VOLTAGE = 3.3

#functie pentru citirea datelor din .csv
def citire(file_path):
    print(f"Se citesc datele din {file_path}")
    failed_items=[]
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        #verificam fiecare data din .csv, iar cele care nu sunt in parametrii le inseram intr-o lista
        for data in reader:
            if (float(data['temperature']) > MAX_TEMP) or (float(data['voltage']) < MIN_VOLTAGE):
                failed_items.append(data)
    return failed_items

def export(date_problema,output_path):
    with open(output_path,"w") as o:
        json.dump(date_problema,o,indent=4)
        

if __name__ == "__main__":
    erori_gasite=citire("raw_sensor_data.csv")
    export(erori_gasite,"failed_tests.json")
    print(f"Au fost gasite {len(erori_gasite)} piese defecte.")