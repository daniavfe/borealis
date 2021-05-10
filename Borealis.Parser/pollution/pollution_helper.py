from measurement import Helper
from measurement import MeasurementAnalyzer
from client import ApiClient
from common import Logger
from datetime import datetime, timedelta
import os

class PollutionHelper(Helper):
    def __init__(self, api_client:ApiClient, logger:Logger) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def get_extension(self) -> str:
        return '.txt'

    def get_usable_file_content(self, file_path:str) -> list:
        # Check file exists
        if not os.path.isfile(file_path):
            raise Exception('File does not exists')

        # Open file
        file = open(file_path, 'r')
        return file.readlines()

    def get_data_content(self, row:str) -> list:
        if row[2] == ',':
            return self.__get_from_comma_separated_content__(row)
        else:
            return self.__get_from_text_content__(row)

    def upload_data(self, items_to_upload:list) -> None:
        # Upload items to API
        self.__api_client__.create_measurements(items_to_upload)

    def pre_upload(self, file_path:str) -> None:
        # Analyze data, upload missing stations and magnitudes, get dates
        measurement_analyzer : MeasurementAnalyzer = MeasurementAnalyzer(self.__logger__)
        measurement_analyzer.analyze_file(file_path)

        # Get data from analyzer
        stations :list = measurement_analyzer.stations
        magnitudes :list = measurement_analyzer.magnitudes
        first_date :datetime = measurement_analyzer.first_date
        last_date :datetime = measurement_analyzer.last_date

        # Check the existence of stations and magnitudes
        missing_stations = self.__api_client__.station_existence(list(stations))
        missing_magnitudes = self.__api_client__.magnitude_existence(list(magnitudes))

        # Create missing station and magnitudes
        self.__api_client__.create_stations(missing_stations)
        self.__api_client__.create_magnitudes(missing_magnitudes)

    def __get_insertable_object__(self, town_id:int, datetime:datetime, magnitude_id:int, station_id:int, data:float, validation_code:str):
        return {"townId": town_id, "datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id, "data": data, "validationCode": validation_code}

    def __get_from_comma_separated_content__(self, row:str)->list:
        items = list()
        component = row.split(',')
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
            items.append(self.__get_insertable_object__(town_id, measurement_datetime,magnitude_id,station_id, data, validation_code))
        return items

    def __get_from_text_content__(self, row:str):
        items = list()
        town_id = int(row[2:5])
        station_id = int(row[5:8])
        magnitude_id = int(row[8:10])
        year = int("20" + row[14:16])
        month = int(row[16:18])
        day = int(row[18:20])
        date = datetime(year, month, day)
        for hour in range(0, 24):
            index = 20 + (hour * 6)
            data = float(row[index: index + 5])
            validation_code = row[index + 5:index + 6]
            measurement_datetime = date + timedelta(hours=hour + 1)
            items.append(self.__get_insertable_object__(town_id, measurement_datetime,magnitude_id,station_id, data, validation_code))
        return items