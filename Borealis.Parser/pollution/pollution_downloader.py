from configuration import PollutionConfiguration
from common import Logger
from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os


class PollutionDownloader():

    def __init__(self, pollution_configuration:PollutionConfiguration, logger:Logger):
        self.__main_page_url__ :str= pollution_configuration.main_page_url
        self.__download_path__ :str= pollution_configuration.download_path
        self.__logger__ = logger

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
        lista = list(map(lambda x: {'year':x.p.text, 'url':'https://datos.madrid.es/' + x.a['href']}, file_list))
        return lista

    def __unzip_file__(self, path):
        self.__logger__.info(f'Unzipping file {path}')
        if os.path.isfile(path):
            directory_path = os.path.splitext(path)[0]
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(directory_path)
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

    def get_available_files(self):
        available_files = self.__get_file_list__()
        self.__create_directory__()
        for file in available_files:
            download_path = os.path.join(self.__download_path__, f'{file["year"]}.zip')
            self.__download_file__(download_path, file['url'])
            self.__unzip_file__(download_path)
        self.__logger__.info(f'All files downloaded')
