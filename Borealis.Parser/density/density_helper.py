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
        #self.__api_client__.create_densities(items_to_upload)
        return

    def pre_upload(self, file_path:str) -> None:
        # Analyze data, upload missing districts and neighborhoods
        return


    def __get_insertable_object__(self, year:int, month:int, district_id:int, neighborhood_id:int, value:float):
        return {'year': year, 'month': month,'district_id': district_id, 'neighborhood_id': neighborhood_id, 'value': value}
