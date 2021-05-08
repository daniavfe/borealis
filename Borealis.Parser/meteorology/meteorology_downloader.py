from configuration import MeteorologyConfiguration
from common import Logger
from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os


class MeteorologyDownloader():

    def __init__(self, meteorology_configuration:MeteorologyConfiguration, logger:Logger)->None:
        self.__main_page_url__ :str = meteorology_configuration.main_page_url
        self.__download_path__ :str= meteorology_configuration.download_path
        self.__logger__ :Logger = logger

    def __download_file__(self, path, url):
        self.__logger__.info(f'Downloading file. Url: {url}')
        response = requests.get(url)
        open(path, 'wb').write(response.content)
        self.__logger__.info(f'File {url} downloaded.')

    def __get_file_list__(self):
        self.__logger__.info(f'Getting file list from url {self.__main_page_url__}')
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        file_list = soup.find(class_="asociada-list")
        files = list()
        for year_section in file_list:
            year = year_section.p.text
            for month_section in year_section.ul:
                month = month_section.p.text
                file = month_section.find_all('a', href=True)[1]
                files.append({'year':year, 'month':month, 'url':'https://datos.madrid.es/'+file['href']})
        return files;

    def __unzip_file__(self, path):
        self.__logger__.info(f'Unzipping file {path}')
        if(os.path.isfile(path)):
            directory_path = os.path.splitext(path)[0]
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(directory_path)
                self.__logger__.info(f'File {path} unzipped')
        else:
            elf.__logger__.warning(f'File {path} does not exist')
    
    def __create_directory__(self, path):
        if not os.path.isdir(path):
            self.__logger__.info(f'Path {self.__download_path__} does not exist. Creating')
            try:
                os.makedirs(path)
            except:
                  self.__logger__.error(f'Error while creating {self.__download_path__}')

    def get_available_files(self):
        available_files = self.__get_file_list__()     
        for file in available_files:
            download_folder_path = os.path.join(self.__download_path__,  file['year'])
            download_path = os.path.join(download_folder_path, file['month']+'.txt')
            self.__create_directory__(download_folder_path)
            self.__download_file__(download_path, file['url'])
        self.__logger__.info(f'All files downloaded')

