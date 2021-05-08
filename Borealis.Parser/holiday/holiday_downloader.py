from configuration import HolidayConfiguration
from common import Logger
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import csv
import json
import os

class HolidayDownloader():
    
    def __init__(self, holiday_configuration:HolidayConfiguration, logger:Logger )->None:
        self.__main_page_url__ = holiday_configuration.main_page_url
        self.__download_path__ = holiday_configuration.download_path
        self.__logger__ :Logger = logger

    def __get_file_list__(self):
        self.__logger__.info(f'Getting file from url {self.__main_page_url__}')
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        item = soup.find(class_="asociada-list")
        return {'url':'https://datos.madrid.es/'+item.a['href']};

    def __download_file__(self, url):
        self.__logger__.info(f'Downloading file {url}')
        response = requests.get(url)
        file_path = os.path.join(self.__download_path__, 'calendar.csv')
        open(file_path, 'wb').write(response.content)
        self.__logger__.info(f'File {url} downloaded')

    def download_calendar(self):
        calendar = self.__get_file_list__()
        if not os.path.isdir(self.__download_path__):
            try:
                os.makedirs(self.__download_path__)
            except:
                 self.__logger__.warning(f"Error while creating directory: {path}")
        self.__download_file__(calendar['url'])


