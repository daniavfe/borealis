from configuration import HolidayConfiguration
from common import Logger
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from .holiday_analyzer import HolidayAnalyzer
from client import ApiClient
import requests
import csv
import json
import os

class HolidayDownloader():
    
    def __init__(self, holiday_configuration:HolidayConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__main_page_url__ :str = holiday_configuration.main_page_url
        self.__download_path__ :str = holiday_configuration.download_path
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def __get_file_list__(self):
        self.__logger__.info(f'Getting file from url {self.__main_page_url__}')
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        item = soup.find(class_="asociada-list")
        return {'url':'https://datos.madrid.es/' + item.a['href']}

    def __download_file__(self, url):
        self.__logger__.info(f'Downloading file {url}')
        response = requests.get(url)
        file_path = os.path.join(self.__download_path__, 'calendar.csv')
        open(file_path, 'wb').write(response.content)
        holiday_analyzer = HolidayAnalyzer(self.__logger__)
        first_date, last_date = holiday_analyzer.analyze_file(file_path)
        file_id = self.__api_client__.create_timeline('Holiday', first_date, last_date, 'Downloaded', file_path)
        file_path_with_id = os.path.join(self.__download_path__, f'{file_id}-calendar.csv')
        os.rename(file_path, file_path_with_id)
        self.__logger__.info(f'File {url} downloaded')

    def download_calendar(self):
        calendar = self.__get_file_list__()
        if not os.path.isdir(self.__download_path__):
            try:
                os.makedirs(self.__download_path__)
            except:
                 self.__logger__.warning(f"Error while creating directory: {path}")
        self.__download_file__(calendar['url'])


