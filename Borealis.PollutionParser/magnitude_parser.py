import requests
import json
import csv

class MagnitudeParser():
    
    def __init__(self):
        self.__base_uri__ = "http://127.0.0.1:5000/api"
        self.__endpoint__= "/pollution/magnitude/"

    def __insert_magnitude__(self, id, name, formula, measurement_unit):
        payload = {"id": id, "name": name, "formula": formula, 'measurementUnit': measurement_unit}    
        requests.post(self.__base_uri__+self.__endpoint__, data=json.dumps(payload))

    def load(self, file_path):
        with open(file_path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                else:
                    self.__insert_magnitude__(row[0], row[1],row[2], row[3])
                    line_count+= 1

        print(f'¡Complete!')
