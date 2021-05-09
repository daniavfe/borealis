from common import Logger
from datetime import datetime
import os
import glob

class MeasurementAnalyzer():

    def __init__(self, logger:Logger):
        self.__logger__ = logger
        self.stations :set = set()
        self.magnitudes :set = set()
        self.first_date :datetime = None
        self.last_date :datetime = None

    def analyze_all_files_in_directory(self, path):
        if not os.path.isdir(path):
            self.__logger__.warning(f'Path {path} is not a directory')
            return
         
        total_station_ids = set()
        total_magnitude_ids = set()
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    station_ids, magnitude_ids = self.analyze_file(os.path.join(root, file))
                    total_station_ids.update(station_ids)
                    total_magnitude_ids.update(magnitude_ids)
                    print(f'{root} {file}')
        self.__logger__.info(f'stations: {sorted(total_station_ids)}')
        elf.__logger__.info(f'magnitudes: {sorted(total_magnitude_ids)}')
        return total_station_ids, total_magnitude_ids

    def analyze_file(self, path):
        if not os.path.isfile(path):
            elf.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    def __analyze__(self, path):
        if not os.path.isfile(path):
            self.__logger__.warning(f'File {path}')
            return

        file = open(path, 'r')
        content = file.readlines()
        number_of_lines = len(content)
        
        self.__logger__.info(f'Analyzing {path}')
        for row in content:
            if row[2] == ',':
               station_id, magnitude_id, date = self.__get_from_comma_separated_content__(row)
            else:
               station_id, magnitude_id, date = self.__get_from_text_content__(row)

            if self.last_date == None or date > self.last_date:
                self.last_date = date
            if self.first_date == None or date < self.first_date:
                self.first_date = date

            self.stations.add(station_id)
            self.magnitudes.add(magnitude_id)
        
        self.__logger__.info(f'Analysis done')

    def __get_from_comma_separated_content__(self, row:str) -> (int, int, datetime):
        component = row.split(',')
        station_id = component[2]
        magnitude_id = component[3]
        technique_id = component[4]
        year = int(component[6])
        month = int(component[7])
        day = int(component[8])
        date = datetime(year, month, day)
        return station_id, magnitude_id, date

    def __get_from_text_content__(self, row:str) -> (int, int, datetime):
        station_id = row[5:8]
        magnitude_id = row[8:10]
        technique_id = row[10:12]
        year = int("20" + row[14:16])
        month = int(row[16:18])
        day = int(row[18:20])
        date = datetime(year, month, day)
        return station_id, magnitude_id, date