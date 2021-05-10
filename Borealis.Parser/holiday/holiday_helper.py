from measurement import Helper
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os
import csv

class HolidayHelper():

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
        day_of_week_switch = {
            'lunes':0,
            'martes': 1,
            'miércoles': 2,
            'jueves':3,
            'viernes': 4,
            'sábado': 5,
            'domingo':6
        }

        scope_switch = {
            'Festivo nacional':'NATIONAL_FESTIVE',
            'Festivo de la Comunidad de Madrid': 'COMMUNITY_FESTIVE',
            'Festivo local de la ciudad de Madrid': 'LOCAL_FESTIVE'
        }

        if row[0] == '':
            return[]

        day_of_week = day_of_week_switch.get(row[1], None)

        scope = scope_switch.get(row[3], None)   
        date = datetime.strptime(row[0], '%d/%m/%Y').strftime('%Y-%m-%d %H:%M:%S')
        name = row[4]
        return self.__get_insertable_object__(date, day_of_week,name, scope)

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        #self.__api_client__.create_holidays(items_to_upload)
        return

    def pre_upload(self, file_path:str) -> None:
        return

    def __get_insertable_object__(self, date:datetime, day_of_week:int, name:str, scope:str) -> list:
        return [{"date":date, "dayOfWeek":day_of_week, "name":name, "scope":scope}]


