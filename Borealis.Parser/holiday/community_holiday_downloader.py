from configuration import HolidayConfiguration
from common import Logger
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from .community_holiday_analyzer import CommunityHolidayAnalyzer
from client import ApiClient
import requests
import csv
import json
import os

class CommunityHolidayDownloader():
    
    def __init__(self, holiday_configuration:HolidayConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__main_page_url__ :str = holiday_configuration.community_main_page_url
        self.__download_path__ :str = holiday_configuration.community_download_path
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger


    def __download_file__(self, url):
        self.__logger__.info(f'Downloading file {url}')
        response = requests.get(url)
        file_path = os.path.join(self.__download_path__, 'calendar.csv')
        open(file_path, 'wb').write(response.content)
        holiday_analyzer = CommunityHolidayAnalyzer(self.__logger__)
        holiday_analyzer.analyze_file(file_path)
        file_id = self.__api_client__.create_timeline('CommunityHoliday', holiday_analyzer.first_date, holiday_analyzer.last_date, 'Downloaded', file_path)
        file_path_with_id = os.path.join(self.__download_path__, f'{file_id}-calendar.csv')
        os.rename(file_path, file_path_with_id)
        self.__logger__.info(f'File {url} downloaded')

    def download_calendar(self):
        if not os.path.isdir(self.__download_path__):
            try:
                os.makedirs(self.__download_path__)
            except:
                 self.__logger__.warning(f"Error while creating directory: {path}")
        self.__download_file__(self.__main_page_url__)


