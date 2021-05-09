from configuration import PollutionConfiguration
from common import Logger
from client import ApiClient
from measurement import CsvMeasurementAnalyzer
from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os


class CommunityPollutionDownloader():

    def __init__(self, pollution_configuration:PollutionConfiguration, api_client:ApiClient, logger:Logger):
        self.__main_page_url__ :str = pollution_configuration.community_main_page_url
        self.__download_path__ :str = pollution_configuration.community_download_path
        self.__api_client__ :ApiClient = api_client
        self.__logger__ = logger

    def __download_file__(self, path,url):
        self.__logger__.info(f'Downloading file. Url: {url}')
        response = requests.get(url)
        open(path, 'wb').write(response.content)        
        self.__logger__.info(f'File {url} downloaded.')

    def __get_file_list__(self):
        self.__logger__.info(f'Getting file list from url {self.__main_page_url__}')
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        file_list = soup.find_all(class_='resource-item')
        lista = list(map(lambda x: {'year':x.find(class_='heading').text.strip(), 'url':x.find(class_='dropdown').find_all('li')[1].a['href']}, file_list))
        lista = list(filter(lambda x: x['url'].find('.zip') != -1, lista))
        return lista

    def __unzip_file__(self, path, folder_path):
        self.__logger__.info(f'Unzipping file {path}')
        if os.path.isfile(path):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                self.__logger__.info(f'File {path} unzipped')
        else:
             self.__logger__.warning(f'File {path} does not exist')

    def __create_directory__(self):
        if not os.path.isdir(self.__download_path__):
            self.__logger__.info(f'Path {self.__download_path__} does not exist. Creating')
            try:
                os.makedirs(self.__download_path__)
            except:
                self.__logger__.error(f'Error while creating {self.__download_path__}')

    def __upload_timeline__(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".csv"):
                      measurement_analyzer = CsvMeasurementAnalyzer(self.__logger__)
                      file_path = os.path.join(root, file)
                      stations, magnitudes, first_date, last_date = measurement_analyzer.analyze_file(file_path)  
                      file_id = self.__api_client__.create_timeline('CommunityPollution', first_date, last_date, 'Downloaded', file_path)
                      file_path_with_id = os.path.join(folder_path,f'{file_id}-{file}')
                      os.rename(file_path, file_path_with_id)

    def get_available_files(self):
        available_files = self.__get_file_list__()
        self.__create_directory__()
        for file in available_files:
            download_path = os.path.join(self.__download_path__, f'{file["year"]}.zip')
            self.__download_file__(download_path, file['url'])
            self.__unzip_file__(download_path, os.path.join(self.__download_path__, file["year"]))
            self.__upload_timeline__(os.path.join(self.__download_path__, file["year"]))
        self.__logger__.info(f'All files downloaded')
