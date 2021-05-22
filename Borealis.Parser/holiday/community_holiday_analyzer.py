from common import Logger
from datetime import datetime
import os
import csv

class CommunityHolidayAnalyzer():
    def __init__(self, logger:Logger):
        self.__logger__ :Logger = logger
        self.first_date: datetime
        self.last_date:datetime


    def __analyze__(self, path):
        first_year = None
        last_year = None
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=';')
            for row in list(csv_reader)[1:]:
                year = int(row[0])
                if first_year == None or first_year > year:
                    first_year = year
                if last_year == None or last_year < year:
                    last_year = year

            self.first_date = datetime(first_year, 1, 1)
            self.last_date =datetime(last_year, 12, 31)


    def analyze_file(self, path):
        if not os.path.isfile(path):
            elf.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    