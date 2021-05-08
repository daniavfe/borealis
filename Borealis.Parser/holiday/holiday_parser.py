from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import requests
import csv
import json

class HolidayParser():
    def __init__(self, api_client:ApiClient, logger:Logger)->None:
        self.__api_client__:ApiClient = api_client
        self.__logger__ :Logger = logger

    def upload_file(self, path):
        self.__logger__.info(f'Uploading {path} file')
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=';')
            line_count = 0

            day_of_week_switch = {
                "lunes":0,
                "martes": 1,
                "miércoles": 2,
                "jueves":3,
                "viernes": 4,
                "sábado": 5,
                "domingo":6,
            }

            scope_switch = {
                'Festivo nacional':'NATIONAL_FESTIVE',
                'Festivo de la Comunidad de Madrid': 'COMMUNITY_FESTIVE',
                'Festivo local de la ciudad de Madrid': 'LOCAL_FESTIVE'
            }

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    day_of_week = day_of_week_switch.get(row[1], '')
                    if day_of_week == '':
                        break
                    scope = scope_switch.get(row[3], '')   
                    date = datetime.strptime(row[0], '%d/%m/%Y').strftime('%Y-%m-%d %H:%M:%S')
                    if(scope != ''):
                        self.__api_client__.create_holiday(date, day_of_week,row[4], scope)
                    line_count += 1
        self.__logger__.info(f'File {path} upload completed')
