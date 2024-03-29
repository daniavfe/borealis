from common import Logger
from datetime import datetime
import os
import csv

class HolidayAnalyzer():
   
    def __init__(self, logger:Logger):
        self.__logger__ :Logger = logger
        self.first_date : datetime = None
        self.last_date :datetime = None

    def __analyze__(self, path):
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=';')
            for row in list(csv_reader)[1:]:
                if not row[0]:
                    break
                holiday_date = datetime.strptime(row[0], '%d/%m/%Y')
                if self.first_date == None or self.first_date > holiday_date:
                    self.first_date = holiday_date
                if self.last_date == None or self.last_date < holiday_date:
                    self.last_date = holiday_date
                        

    def analyze_file(self, path):
        if not os.path.isfile(path):
            elf.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    