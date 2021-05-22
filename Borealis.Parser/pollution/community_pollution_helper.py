from measurement import Helper
from measurement import MeasurementCsvAnalyzer
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os
import csv

class CommunityPollutionHelper(Helper):
    
    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def get_extension(self) -> str:
        return '.csv'

    def get_section_size(self):
        return 20

    def get_thread_number(self):
        return 30

    def get_usable_file_content(self, file_path:str) -> list:
        # Check file exists
        if not os.path.isfile(file_path):
            raise Exception('File does not exists')

        # Open file
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            return list(reader)[1:]

    def get_data_content(self, row:str) -> dict:
        items = dict()
        town_id = int(row[1])
        station_id = row[2]
        magnitude_id = row[3]
        year = int(row[5])
        month = int(row[6])
        day = int(row[7])
        date = datetime(year, month, day)
        for hour in range(0, 24):
            index = 8 + (hour * 2)
            validation_code = row[index + 1].strip()
            if validation_code == 'N':
                continue
            data = float(row[index])
            measurement_datetime = date + timedelta(hours=hour + 1)
            item_key = self. __get__insertable__object__key__(town_id, measurement_datetime,magnitude_id,station_id)
            items[item_key] = self.__get_insertable_object__(town_id, measurement_datetime,magnitude_id,station_id, data, validation_code)     
        return items

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        self.__api_client__.create_measurements(items_to_upload)

    def pre_upload(self, file_path:str) -> None:
        # Analyze data, upload missing stations and magnitudes, get dates
        measurement_analyzer : MeasurementAnalyzer = MeasurementCsvAnalyzer(self.__logger__)
        measurement_analyzer.analyze_file(file_path)

        # Get data from analyzer
        stations :list = measurement_analyzer.stations
        magnitudes :list = measurement_analyzer.magnitudes
        towns:list = measurement_analyzer.towns
        first_date :datetime = measurement_analyzer.first_date
        last_date :datetime = measurement_analyzer.last_date

        # Check the existence of stations and magnitudes
        missing_towns = self.__api_client__.town_existence(list(towns))
        missing_stations = self.__api_client__.station_existence(list(stations))
        missing_magnitudes = self.__api_client__.magnitude_existence(list(magnitudes))

        # Create missing station and magnitudes
        self.__api_client__.create_towns(missing_towns)
        self.__api_client__.create_stations(missing_stations)
        self.__api_client__.create_magnitudes(missing_magnitudes)
    
    def __get__insertable__object__key__(self, town_id:int, datetime:datetime, magnitude_id:int, station_id:int):
        return f'{town_id}{datetime.strftime("%Y-%m-%d %H:%M:%S")}{station_id}{magnitude_id}'

    def __get_insertable_object__(self, town_id:int, datetime:datetime, magnitude_id:int, station_id:int, data:float, validation_code:str):
        return {"townId": town_id, "datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id, "data": data, "validationCode": validation_code}
