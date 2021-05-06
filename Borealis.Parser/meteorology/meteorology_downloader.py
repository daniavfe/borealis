from configuration import MeteorologyConfiguration
from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os


class MeteorologyDownloader():

    def __init__(self, meteorology_configuration:MeteorologyConfiguration)->None:
        self.__main_page_url__ :str = meteorology_configuration.main_page_url
        self.__download_path__ :str= meteorology_configuration.download_path

    def __download_file__(self, path, url):
        print(f'Downloading file {url}')
        response = requests.get(url)
        open(path, 'wb').write(response.content)
        print(f'File {url} dopwnloaded')

    def __get_file_list__(self):
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
        print(f'Unzipping file {path}')
        if(os.path.isfile(path)):
            directory_path = os.path.splitext(path)[0]
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(directory_path)
            print(f'File {path} unzipped')
        else:
            print(f'File {path} does not exist')
    
    def __create_directory__(self, path):
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except:
                print(f"Error while creating directory: {path}")

    def get_available_files(self):
        available_files = self.__get_file_list__()     
        for file in available_files:
            download_folder_path = os.path.join(self.__download_path__,  file['year'])
            download_path = os.path.join(download_folder_path, file['month']+'.txt')
            self.__create_directory__(download_folder_path)
            self.__download_file__(download_path, file['url'])

