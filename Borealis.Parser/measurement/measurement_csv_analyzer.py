from common import Logger
from datetime import datetime
import os
import csv

class MeasurementCsvAnalyzer():

    def __init__(self, logger:Logger):
        self.__logger__ = logger
        self.stations :set = set()
        self.magnitudes :set = set()
        self.towns :set = set()
        self.first_date :datetime = None
        self.last_date :datetime = None

    def analyze_file(self, path):
        if not os.path.isfile(path):
            self.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    def __analyze__(self, path):
        if not os.path.isfile(path):
            self.__logger__.warning(f'File {path}')
            return
        self.__logger__.info(f'Analyzing {path}')

        with open(path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            content = list(reader)[1:]

            for row in content:
                town_id = row[1]
                station_id = row[2]
                magnitude_id = row[3]
                year = int(row[5])
                month = int(row[6])
                day = int(row[7])
                date = datetime(year, month, day)

                if self.last_date == None or date > self.last_date:
                    self.last_date = date
                if self.first_date == None or date < self.first_date:
                    self.first_date = date

                self.towns.add(town_id)
                self.stations.add(station_id)
                self.magnitudes.add(magnitude_id)
        
            self.__logger__.info(f'Analysis done')
