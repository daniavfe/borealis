from common import Logger
from datetime import datetime
import os
import csv

class HolidayAnalyzer():
    def __init__(self, logger:Logger):
        self.__logger__ :Logger = logger


    def __analyze__(self, path):
        first_date = None
        last_date = None
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        if not row[0]:
                            break
                        holiday_date = datetime.strptime(row[0], '%d/%m/%Y')
                        if first_date == None or first_date > holiday_date:
                            first_date = holiday_date
                        if last_date == None or last_date < holiday_date:
                            last_date = holiday_date
                        line_count += 1
        return first_date, last_date


    def analyze_file(self, path):
        if not os.path.isfile(path):
            elf.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    