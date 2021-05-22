from measurement import Helper
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os
import csv

class CommunityHolidayHelper():

    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def get_extension(self) -> str:
        return '.csv'

    def get_section_size(self):
        return 200

    def get_thread_number(self):
        return 1

    def get_usable_file_content(self, file_path:str) -> dict:
        # Check file exists
        if not os.path.isfile(file_path):
            raise Exception('File does not exists')

        # Open file
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[1:]

    def get_data_content(self, row:str) -> list:      
        items = dict()
        date = datetime.strptime(row[5], '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
        name = 'festivo'
        scope = 'LOCAL_FESTIVE'
        town_id = int(row[1])
        item_key = self. __get__insertable__object__key__(town_id, date)
        items[item_key] =self.__get_insertable_object__(date, -1, name, scope, town_id)
        return items

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        self.__api_client__.create_holidays(items_to_upload)
        return

    def pre_upload(self, file_path:str) -> None:
        return

    def __get__insertable__object__key__(self, town_id:int, date:datetime):
        return f'{town_id}{date}'

    def __get_insertable_object__(self, date:datetime, day_of_week:int, name:str, scope:str, town_id:int) -> list:
        return {"date":date, "dayOfWeek":day_of_week, "name":name, "scope":scope, "townId":town_id}


