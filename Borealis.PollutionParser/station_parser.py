from datetime import datetime, timedelta
import requests
import json
import csv

class StationParser():
    def __init__(self):
        self.base_uri = "http://127.0.0.1:5000/api"
        self.endpoint= "/pollution/station/"

    def __insert_station__(self, id, name, address, longitude, latitude, altitude,  start_date, end_date):

        payload = {"id": id, "name": name, "address": address,
                   "latitude": latitude, "longitude": longitude}

        if start_date:
            payload['startDate']= datetime.strptime(start_date, '%d/%m/%Y %H:%M').strftime("%Y-%m-%d %H:%M:%S")

        if end_date:
            payload['endDate'] = datetime.strptime(end_date, '%d/%m/%Y %H:%M').strftime("%Y-%m-%d %H:%M:%S")

        if altitude:
            payload['altitude'] = int(altitude)


        #print(json.dumps(payload))
        requests.post(self.base_uri+self.endpoint, data=json.dumps(payload))


    def load(self, file_path):
        with open(file_path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                else:
                    self.__insert_station__(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7])
                    line_count+= 1
        print(f'¡Complete!')


