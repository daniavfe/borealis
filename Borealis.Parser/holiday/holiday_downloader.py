from configuration import HolidayConfiguration
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import csv
import json
import os

class HolidayDownloader():
    
    def __init__(self, holiday_configuration:HolidayConfiguration)->None:
        self.__main_page_url__ = holiday_configuration.main_page_url
        self.__download_path__ = holiday_configuration.download_path

    def __get_file_list__(self):
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        item = soup.find(class_="asociada-list")
        #lista = list(map(lambda x: {'url':'https://datos.madrid.es/'+x.a['href']}, file_list))
        return {'url':'https://datos.madrid.es/'+item.a['href']};

    def __download_file__(self, url):
        print(f'Downloading file {url}')
        response = requests.get(url)
        file_path = os.path.join(self.__download_path__, 'calendar.csv')
        open(file_path, 'wb').write(response.content)
        print(f'File {url} downloaded')

    def download_calendar(self):
        calendar = self.__get_file_list__()
        if not os.path.isdir(self.__download_path__):
            try:
                os.makedirs(self.__download_path__)
            except:
                print(f"Error while creating directory: {path}")
        self.__download_file__(calendar['url'])


