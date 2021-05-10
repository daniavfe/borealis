from measurement import Helper
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os
import csv

class DensityHelper(Helper):
    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def get_extension(self) -> str:
        return '.csv'

    def get_section_size(self):
        return 200

    def get_thread_number(self):
        return 20

    def get_usable_file_content(self, file_path:str) -> list:
        # Check file exists
        if not os.path.isfile(file_path):
            raise Exception('File does not exists')

        # Open file
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[1:]

    def get_data_content(self, row:str) -> list:
        return self.__get_insertable_object__(row[0], row[1], row[2], row[4], row[6])

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        self.__api_client__.create_densities(items_to_upload)
        return

    def pre_upload(self, file_path:str) -> None:
        # Analyze data, upload missing districts and neighborhoods
        with open(file_path) as csv_file:
            reader = list(csv.reader(csv_file, delimiter=';'))[1:]
            district_list = self.__api_client__.get_existing_districts(1, 1000)
            neighborhood_list = self.__api_client__.get_existing_neighborhoods(1, 1000)

            for row in reader:
                district_id = int(row[2])
                district_name = row[3]                                   
                neighborhood_id = int(row[4])
                neighborhood_name = row[5]

                if not district_id in district_list:
                    self.__logger__.info(f'District {district_name} not found. Creating')
                    self.__api_client__.create_district(district_id, district_name, 0.0)
                    district_list.add(district_id)
                    self.__logger__.info(f'District {district_name} created with id {district_id}')

                if not neighborhood_id in neighborhood_list:
                    self.__logger__.info(f'Neighborhood {neighborhood_name} not found. Creating')
                    self.__api_client__.create_neighborhood(neighborhood_id, district_id, neighborhood_name, 0.0)
                    neighborhood_list.add(neighborhood_id)
                    self.__logger__.info(f'Neighborhood {neighborhood_name} created with id {neighborhood_id}')

        return


    def __get_insertable_object__(self, year:int, month:int, district_id:int, neighborhood_id:int, value:float):
        return [{'year': year, 'month': month,'districtId': district_id, 'neighborhoodId': neighborhood_id, 'value': value}]
