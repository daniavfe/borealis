from datetime import datetime, timedelta
from common import Logger
import requests
import json
import sys
import os
import threading
import math
from .measurement_analyzer import MeasurementAnalyzer
from client import ApiClient

class MeasurementParser():

    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger= logger
        
    def __get_insertable_object__(self, town_id:int, datetime:datetime, magnitude_id:int, station_id:int, data:float, validation_code:str):
        return {"townId": town_id, "datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id, "data": data, "validationCode": validation_code}
    
    def upload_all_files(self, path:str) -> None:
        if not os.path.isdir(path):
            self.__logger__.info(f'Path {path} is not a directory')
            return
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    self.load_with_parallelism(os.path.join(root, file))

    # Deprecated
    def load(self, file_path:str) -> None:
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
                self.__logger__.info(f'Progress: {number_of_processedItems *100/number_of_items} %')

        if len(accumulated_items_to_upload) > 0:
          items_not_uploaded.extend(self.__insert_accumulated_measurements__(accumulated_items_to_upload))

    def load_with_parallelism(self, file_path:str, section_size:int=20, thread_number:int=30)->None:
        
        self.__section__index = 0
        self.__section_lock__ = threading.Lock()
        self.__section_size__ = section_size
        self.__thread_number__ = thread_number

        start_date = datetime.now()
        file = open(file_path, 'r')
        self.__file_content__ = file.readlines()
        self.__number_of_sections__ = math.floor(len(self.__file_content__) / self.__section_size__)

        size = len(self.__file_content__)
        threads = [threading.Thread] * self.__thread_number__

        self.__logger__.info(f'Uploading file {file_path}.Size: {size}. Section size: {self.__section_size__}. Nº of sections: {self.__number_of_sections__}. Thread number: {self.__thread_number__}')
        #Analizar fichero para sacar las estaciones y magnitudes que se están
        #utilizando

        measurement_analyzer = MeasurementAnalyzer(self.__logger__)
        stations, magnitudes = measurement_analyzer.analyze_file(file_path)

        not_created_stations = self.__api_client__.station_existence(list(stations))
        not_created_magnitudes = self.__api_client__.magnitude_existence(list(magnitudes))

        self.__logger__.info(f'Missing stations {",".join(not_created_stations)}')
        self.__logger__.info(f'Missing magnitudes {",".join(not_created_magnitudes)}')
        
        self.__api_client__.create_stations(not_created_stations)
        self.__api_client__.create_magnitudes(not_created_magnitudes)

        for index in range(0, self.__thread_number__):
            i = index
            threads[index] = threading.Thread(target = self.__process_item__, args = [i])
            threads[index].start()

        for index in range(0, self.__thread_number__):
            threads[index].join()

        end_date = datetime.now()
  
    def __process_item__(self, thread_number:int)->None:
        self.__logger__.debug(f"Hilo {thread_number} en marcha")
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
                    town_id = int(component[1])
                    station_id = int(component[2])
                    magnitude_id = int(component[3])
                    year = int(component[6])
                    month = int(component[7])
                    day = int(component[8])
                    date = datetime(year, month, day)
                    for hour in range(0, 24):
                        index = 9 + (hour * 2)
                        data = float(component[index])
                        validation_code = component[index + 1].strip()
                        measurement_datetime = date + timedelta(hours=hour + 1)
                        accumulated_items_to_upload.append(self.__get_insertable_object__(town_id, measurement_datetime,magnitude_id,station_id, data, validation_code))
                else:
                    town_id = int(line[2:5])
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
                        accumulated_items_to_upload.append(self.__get_insertable_object__(town_id, measurement_datetime,magnitude_id,station_id, data, validation_code))
      
                if len(accumulated_items_to_upload) >= items_to_upload_threshold:
                    self.__api_client__.create_measurements(accumulated_items_to_upload)
                    accumulated_items_to_upload.clear()
                    
            if len(accumulated_items_to_upload) > 0:
                self.__api_client__.create_measurements(accumulated_items_to_upload)

            content = self.__get_file_section__()
        self.__logger__.debug(f"Hilo {thread_number} terminó")

    #devuelve la sección correspondiente al fichero que tiene que procesar
    def __get_file_section__(self)->list:
        self.__section_lock__.acquire()
        if(self.__section__index > self.__number_of_sections__):
            self.__section_lock__.release()
            return None

        start_element_index = self.__section__index * self.__section_size__
        posible_end_element_index = ((self.__section__index + 1) * self.__section_size__)

        if(posible_end_element_index >= len(self.__file_content__)):
            end_element_index = len(self.__file_content__)
        else:     
            end_element_index = posible_end_element_index

        self.__logger__.debug(f'start: {start_element_index}, end:{end_element_index}')

        self.__section__index += 1

        self.__section_lock__.release()

        return self.__file_content__[start_element_index:end_element_index]
        
