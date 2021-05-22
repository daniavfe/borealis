from measurement import Helper
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os
import csv

class CommunityDensityHelper(Helper):
    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def get_extension(self) -> str:
        return '.csv'

    def get_section_size(self):
        return 200

    def get_thread_number(self):
        return 10

    def get_usable_file_content(self, file_path:str) -> list:
        # Check file exists
        if not os.path.isfile(file_path):
            raise Exception('File does not exists')

        # Open file
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[1:]

    def get_data_content(self, row:str) -> list:
        items = dict()
        item_key = self. __get__insertable__object__key__(row[0], 0, row[1], row[1], row[1])
        items[item_key] = self.__get_insertable_object__(row[0], 0, row[1], row[1], row[1], row[3] if row[3] else 0)
        return items

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        self.__api_client__.create_densities(items_to_upload)
        return

    def pre_upload(self, file_path:str) -> None:
        # Analyze data, upload missing districts and neighborhoods
        with open(file_path) as csv_file:
            reader = list(csv.reader(csv_file, delimiter=';'))[1:]
            town_list = self.__api_client__.get_existing_towns(1, 1000)
            district_list = self.__api_client__.get_existing_districts(1, 1000)
            neighborhood_list = self.__api_client__.get_existing_neighborhoods(1, 1000)
           
            for row in reader:
                town_id = int(row[1])
                name = row[2]

                if not town_id in town_list:
                    self.__logger__.info(f'Town {name} not found. Creating')
                    self.__api_client__.create_town(town_id, name)
                    town_list.add(town_id)
                    self.__logger__.info(f'Town {name} created with id {town_id}')

                if not town_id in district_list:
                    self.__logger__.info(f'District {name} not found. Creating')
                    self.__api_client__.create_district(town_id,town_id, name, 0.0)
                    district_list.add(town_id)
                    self.__logger__.info(f'District {name} created with id {town_id}')

                if not town_id in neighborhood_list:
                    self.__logger__.info(f'Neighborhood {name} not found. Creating')
                    self.__api_client__.create_neighborhood(town_id,town_id, name, 0.0)
                    neighborhood_list.add(town_id)
                    self.__logger__.info(f'Neighborhood {name} created with id {town_id}')

        return

    def __get__insertable__object__key__(self, year:int, month:int, town_id:int,  district_id:int, neighborhood_id:int):
        return f'{town_id}{year}{month}{district_id}{neighborhood_id}'

    def __get_insertable_object__(self, year:int, month:int, town_id:int,  district_id:int, neighborhood_id:int, value:float):
        return {'year': year, 'month': month,'townId':town_id, 'districtId': district_id, 'neighborhoodId': neighborhood_id, 'value': value}
