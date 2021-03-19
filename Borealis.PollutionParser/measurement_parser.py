from datetime import datetime, timedelta
import requests
import json
import sys
import os


class MeasurementParser():

    def __init__(self, path):
        self.__base_uri__ = "http://127.0.0.1:5000/api"
        self.__endpoint__= "/pollution"
        self.__path__ = path
        self.magnitudes = set()
        self.stations = set()

    def __insert_measurement__(self, datetime, magnitude_id, station_id, data, validation_code):
        payload = {"datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id,
                   "data": data, "validationCode": validation_code}
        self.magnitudes.add(magnitude_id)
        self.stations.add(station_id)
        #requests.post(self.__base_uri__+self.__endpoint__, data=json.dumps(payload))

    def load_from_folder(self, folder_path):
        return

    def load_txt(self, file_path):
        file = open(file_path, 'r')
        lines = file.readlines()
        number_of_items = len(lines)
        number_of_processedItems = 0
        percentage = 0.0 
 
        #Antes de octubre de 2017
        # Strips the newline character
        for line in lines:
            #province = line[0:2]
            #town = line[2:5]
            station_id = int(line[5:8])
            magnitude_id = int(line[8:10])
            #method = line[10:12]
            #analysis_period = line[12:14]
            date = datetime(int("20"+line[14:16]), int(line[16:18]), int(line[18:20]))
            count = 0
            while count < 24:
                index = 20 + (count * 6)
                data = float(line[index: index+5])
                validation_code = line[index+5:index+6]
                count += 1
                measurement_datetime = date + timedelta(hours=count)
                self.__insert_measurement__(measurement_datetime,magnitude_id,station_id, data, validation_code  )

        

            number_of_processedItems += 1
            percentage = number_of_processedItems / number_of_items * 100
            sys.stdout.flush()
            print(f'{percentage} %')
        print(self.magnitudes)
        print(self.stations)

    def load_csv(self, file_path, delimiter):
        with open(file_path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=delimiter)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                else:
                    self.__insert_magnitude__(row[0], row[1],row[2], row[3])
                    line_count+= 1

    

