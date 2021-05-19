from bs4 import BeautifulSoup
from datetime import datetime,date, timedelta
from common import Logger
from configuration import DensityConfiguration
from client import ApiClient
import requests
import csv
import json
import os


class CommunityDensityDownloader():
   
    def __init__(self, density_configuration:DensityConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__main_page_url__ :str = density_configuration.community_main_page_url
        self.__data_page_url__ :str = density_configuration.community_data_page_url
        self.__download_path__ :str = density_configuration.community_download_path
        self.__api_client__:ApiCLient = api_client
        self.__logger__ :Logger = logger

    def __get_available_years__(self):
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        year_list = list(map(lambda x: int(x.text), soup.find('select', {'id': 'periodo'}).findChildren()))
        return year_list

    def __get_data_values_from_table__(self, item:object):
        item_key = item.find('td', {"class" : "CabTab0"}).text.split('/')[1].strip()
        item_value = int(item.find('td', {"class" : "DatTab"}).text.replace('.', ''))
        return item_key, item_value

    def __get_density__(self, year:int):
        data = {'periodo':f'28~{year}'}
        response = requests.post(self.__data_page_url__, data=data)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            table = soup.find('table', {'id':'tablaDatos'})
            tbody = table.find('tbody')
            items = list(map(lambda x : self.__get_formatted_item__(year, x.th.text, x.td.text), tbody.find_all('tr', recursive=False)[1:]))
            return items
        except:
            return []

    def __get_formatted_item__(self, year, name, value):
        splitted_item = name.split(sep=' ', maxsplit=1)
        id = int(splitted_item[0][2:])
        complete_name = splitted_item[1].strip()
        val = value.replace('.', '')
        if ',' in complete_name:
            divided_name = complete_name.split(',')
            complete_name = f'{divided_name[1]} {divided_name[0]}'

        return {'year':year,'townId':id, 'name': complete_name, 'value':val}


    def __write_csv_file__(self, data: list, year:int):
        complete_path = os.path.join(self.__download_path__, str(year))
        if not os.path.isdir(complete_path):
            try:
                os.makedirs(complete_path)
            except:
                 self.__logger__.error(f"Error while creating directory: {path}")

        file_path = os.path.join(complete_path, f'{year}.csv')
        keys = data[0].keys()

        with open(file_path, 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys,  delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(data)

        file_id = self.__api_client__.create_timeline('CommunityDensity', date(year, 1,1),date(year, 12,31), 'Downloaded', file_path)
        complete_path_with_id= os.path.join(complete_path,f'{file_id}-{year}.csv')
        os.rename(file_path, complete_path_with_id)
        self.__logger__.info(f'file created {file_path} created')

    def download_density_file(self, years=[]):
        self.__logger__.info(f'Downloading density files: Years: {",".join(years)}')
        year_list = self.__get_available_years__()  
        if years != []:
            selected_year_list = list(set(year_list).intersection(set(years)))
        else:
            selected_year_list = year_list

        for year in selected_year_list:  
            densities = self.__get_density__(year)
            self.__write_csv_file__(densities, year)
        self.__logger__.info(f'Density data downloaded')
        
