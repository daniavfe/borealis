from bs4 import BeautifulSoup
import requests
import csv
import json
import zipfile
import os


class MeteorologyDownloader():

    def __init__(self, page_url, download_path):
        self.__page_url__ = page_url
        self.__download_path__ = download_path

    def __download_file__(self, path, url):
        print(f'Downloading file {url}')
        response = requests.get(url)
        open(path, 'wb').write(response.content)
        print(f'File {url} dopwnloaded')

    def __get_file_list__(self):
        response = requests.get(self.__page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        file_list = soup.find(class_="asociada-list")
        #lista = list(map(lambda x: {'year':x.p.text, 'url':'https://datos.madrid.es/'+x.a['href']}, file_list))
        lista = list(map(lambda x: {'year':x.p.text, 'url':'https://datos.madrid.es/'+x.find_all('a', href=True)[1]['href']}, file_list))
        return lista;

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
            download_path = os.path.join(download_folder_path, file['year']+'.txt')
            self.__create_directory__(download_folder_path)
            self.__download_file__(download_path, file['url'])

