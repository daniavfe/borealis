from configuration import TrafficConfiguration
from client import ApiClient
from common import Logger
from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os

class TrafficPointDownloader():

    def __init__(self, traffic_configuration:TrafficConfiguration,api_client:ApiClient, logger:Logger) -> None:
        self.__main_page_url__ :str = traffic_configuration.point_page_url
        self.__download_path__ :str = traffic_configuration.download_path
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    def __download_file__(self, path, file_name, url):
        self.__logger__.info(f'Downloading file. Url: {url}')
        response = requests.get(url)
        complete_path = os.path.join(path,file_name)
        open(complete_path, 'wb').write(response.content)
        self.__logger__.info(f'File {url} downloaded.')

    def __get_file_list__(self):
        self.__logger__.info(f'Getting file list from url {self.__main_page_url__}')
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        file_list = soup.find(class_="asociada-list")
        files = list()
        for year_section in file_list:
            year = year_section.p.text
            for date_section in year_section.ul:
                date = date_section.p.text
                file = date_section.find_all('a', href=True)
                if(len(file) > 1):
                    selected_file = file[2]
                else:
                    selected_file = file[0]
                files.append({'year':year, 'date':date.replace('/', '-'), 'url':'https://datos.madrid.es/' + selected_file['href']})
        return files

    def __unzip_file__(self, path, folder_path):
        self.__logger__.info(f'Unzipping file {path}')
        if os.path.isfile(path):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                self.__logger__.info(f'File {path} unzipped')
        else:
             self.__logger__.warning(f'File {path} does not exist')
    
    def __create_directory__(self, path):
        if not os.path.isdir(path):
            self.__logger__.info(f'Path {self.__download_path__} does not exist. Creating')
            try:
                os.makedirs(path)
            except:
                  self.__logger__.error(f'Error while creating {self.__download_path__}')

    def __upload_timeline__(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                      measurement_analyzer = MeasurementAnalyzer(self.__logger__)
                      file_path = os.path.join(root, file)
                      stations, magnitudes, first_date, last_date = measurement_analyzer.analyze_file(file_path)  
                      file_id = self.__api_client__.create_timeline('Pollution', first_date, last_date, 'Downloaded', file_path)
                      file_path_with_id = os.path.join(folder_path,f'{file_id}-{file}')
                      os.rename(file_path, file_path_with_id)

    def get_available_files(self):
        available_files = self.__get_file_list__()     
        for file in available_files:
            download_folder_path = os.path.join(self.__download_path__,'point',file['year'])
            file_name = f'{file["date"]}.zip'
            self.__create_directory__(download_folder_path)
            self.__download_file__(download_folder_path, file_name, file['url'])
            self.__unzip_file__(os.path.join(download_folder_path, file_name), download_folder_path)
            #self.__upload_timeline__(os.path.join(self.__download_path__, file["year"]))
        self.__logger__.info(f'All files downloaded')

