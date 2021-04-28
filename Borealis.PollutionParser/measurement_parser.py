from datetime import datetime, timedelta
from operator import itemgetter 
import requests
import json
import sys
import os
import threading
import math


class MeasurementParser():

    def __init__(self, section_size = 50, thread_number = 20):
        self.__base_uri__ = "http://127.0.0.1:5000/api"
        self.__endpoint__ = "/pollution"

        self.__section__index = 0
        self.__file_content__ = None
        self.__number_of_sections__ = None

        self.__not_uploaded_lock = threading.Lock()
        self.__not_uploaded_list = []

        self.__section_lock__ = threading.Lock()
        self.__section_size__ = section_size
        self.__thread_number__ = thread_number

    def __insert_measurement__(self, datetime, magnitude_id, station_id, data, validation_code):
        payload = {"datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id,
                   "data": data, "validationCode": validation_code}
        requests.post(self.__base_uri__+self.__endpoint__,
        data=json.dumps(payload))

    def __insert_accumulated_measurements__(self, measurements):
        #print(f'Inserted many {len(measurements)}')
        response = requests.post(self.__base_uri__ + self.__endpoint__ + '/many', data=json.dumps(measurements))
        items_not_created = json.loads(response.content)['itemsNotCreatedPositions']

        if len(items_not_created) > 0:
            return itemgetter(*items_not_created)(measurements)
        
        return []

    def __get_insertable_object__(self, datetime, magnitude_id, station_id, data, validation_code):
        return {"datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id, "data": data, "validationCode": validation_code}

    def __write_not_inserted_items__(self, not_inserted_measurements, path):
        file = open(path, "w")
        data = json.dump(not_inserted_measurements)
        file.write(data)
        file.close()

    def __complete_upload__(self, file, name, year, month):
        print(f'Upload completed')
        #insertar evento que terminó la subida de x fichero

    def load(self, file_path):
        file = open(file_path, 'r')
        content = file.readlines()
        number_of_items = len(content)
        number_of_processedItems = 0
 
        station_id = -1
        magnitude_id = -1
        year = -1
        month = -1
        day = -1

        items_to_upload_threshold = 500
        accumulated_items_to_upload = []
        items_not_uploaded = []

        for line in content:
            if line[2] == ',':
                component = line.split(',')
                station_id = int(component[2])
                magnitude_id = int(component[3])
                year = int(component[6])
                month = int(component[7])
                day = int(component[8])
                date = datetime(year, month, day)
                for hour in range(0, 24):
                    index = 9 + (hour * 2)
                    data = float(component[index])
                    validation_code = component[index + 1]
                    measurement_datetime = date + timedelta(hours=hour + 1)
                    accumulated_items_to_upload.append(self.__get_insertable_object__(measurement_datetime,magnitude_id,station_id, data, validation_code))
            else:
                station_id = int(line[5:8])
                magnitude_id = int(line[8:10])
                year = int("20" + line[14:16])
                month = int(line[16:18])
                day = int(line[18:20])
                date = datetime(year, month, day)
                for hour in range(0, 24):
                    index = 20 + (hour * 6)
                    data = float(line[index: index + 5])
                    validation_code = line[index + 5:index + 6]
                    measurement_datetime = date + timedelta(hours=hour + 1)
                    accumulated_items_to_upload.append(self.__get_insertable_object__(measurement_datetime,magnitude_id,station_id, data, validation_code))

            
            number_of_processedItems += 1
            if len(accumulated_items_to_upload) >= items_to_upload_threshold:
                items_not_uploaded.extend(self.__insert_accumulated_measurements__(accumulated_items_to_upload))
                accumulated_items_to_upload.clear()
                print(f'Progress: {number_of_processedItems *100/number_of_items} %')

        if len(accumulated_items_to_upload) > 0:
          items_not_uploaded.extend(self.__insert_accumulated_measurements__(accumulated_items_to_upload))

        self.__complete_upload__(file_path, 'name', 2009, "Abril")

    def load_with_parallelism(self, file_path):
        start_date = datetime.now()
        file = open(file_path, 'r')
        self.__file_content__ = file.readlines()
        self.__number_of_sections__ = math.floor(len(self.__file_content__) / self.__section_size__)

        size = len(self.__file_content__)
        threads = [threading.Thread]*self.__thread_number__

        for index in range(0, self.__thread_number__):
            i = index
            threads[index] = threading.Thread(target = self.__process_item__, args = [i])
            threads[index].start()

        for index in range(0, self.__thread_number__):
            threads[index].join()

        end_date = datetime.now()

        print(f'Start date: {start_date}, End date: {end_date}')
  
    def __process_item__(self, thread_number):
        print(f"Hilo {thread_number} en marcha")
        content = self.__get_file_section__()

        items_to_upload_threshold = 100
        accumulated_items_to_upload = []

        while(content != None):      
            for line in content:
                station_id = -1
                magnitude_id = -1
                year = -1
                month = -1
                day = -1
                if line[2] == ',':
                    component = line.split(',')
                    station_id = int(component[2])
                    magnitude_id = int(component[3])
                    year = int(component[6])
                    month = int(component[7])
                    day = int(component[8])
                    date = datetime(year, month, day)
                    for hour in range(0, 24):
                        index = 9 + (hour * 2)
                        data = float(component[index])
                        validation_code = component[index + 1]
                        measurement_datetime = date + timedelta(hours=hour + 1)
                        accumulated_items_to_upload.append(self.__get_insertable_object__(measurement_datetime,magnitude_id,station_id, data, validation_code))
                else:
                    station_id = int(line[5:8])
                    magnitude_id = int(line[8:10])
                    year = int("20" + line[14:16])
                    month = int(line[16:18])
                    day = int(line[18:20])
                    date = datetime(year, month, day)
                    for hour in range(0, 24):
                        index = 20 + (hour * 6)
                        data = float(line[index: index + 5])
                        validation_code = line[index + 5:index + 6]
                        measurement_datetime = date + timedelta(hours=hour + 1)
                        accumulated_items_to_upload.append(self.__get_insertable_object__(measurement_datetime,magnitude_id,station_id, data, validation_code))
      
                if len(accumulated_items_to_upload) >= items_to_upload_threshold:
                    not_uploaded_items = self.__insert_accumulated_measurements__(accumulated_items_to_upload)
                    accumulated_items_to_upload.clear()
                    #if(len(not_uploaded_items) > 0):
                        #self.__section_lock__.acquire()
                        #self.__not_uploaded_list.extend(not_uploaded_items)
                        #self.__section_lock__.release()
                    
                if len(accumulated_items_to_upload) > 0:
                    not_uploaded_items = self.__insert_accumulated_measurements__(accumulated_items_to_upload)
                    accumulated_items_to_upload.clear()
                    #if(len(not_uploaded_items) > 0):
                       # self.__section_lock__.acquire()
                       #self.__not_uploaded_list.extend(not_uploaded_items)
                       # self.__section_lock__.release()
            content = self.__get_file_section__()

        print(f"Hilo {thread_number} terminó")

    #devuelve la sección correspondiente al fichero que tiene que procesar
    def __get_file_section__(self):
        self.__section_lock__.acquire()
        if(self.__section__index > self.__number_of_sections__):
            self.__section_lock__.release()
            return None

        start_element_index = self.__section__index * self.__section_size__
        posible_end_element_index = ((self.__section__index + 1) * self.__section_size__)+1

        if(posible_end_element_index >= len(self.__file_content__)):
            end_element_index = len(self.__file_content__)
        else:     
            end_element_index = posible_end_element_index

        print(f'start: {start_element_index}, end:{end_element_index}')

        self.__section__index += 1

        self.__section_lock__.release()

        return self.__file_content__[start_element_index:end_element_index]
        
