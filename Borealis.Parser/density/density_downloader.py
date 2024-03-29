from bs4 import BeautifulSoup
from datetime import datetime,date, timedelta
from common import Logger
from configuration import DensityConfiguration
from client import ApiClient
import requests
import csv
import json
import os


class DensityDownloader():
   
    def __init__(self, density_configuration:DensityConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__main_page_url__ :str = density_configuration.main_page_url
        self.__data_page_url__ :str = density_configuration.data_page_url
        self.__download_path__ :str = density_configuration.download_path
        self.__api_client__:ApiCLient = api_client
        self.__logger__ :Logger = logger

    def __get_districts_and_years__(self):
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        district_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectDistrito"}).findChildren()))[1:]
        year_list = list(map(lambda x:int(x['value'].strip()), soup.find(attrs={"name" : "selectAnio"}).findChildren()))
        return district_list, year_list

    def __get_available_months_and_zones__(self, year:int, district:str):
        data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':'','selectDistrito':district,
                'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'}
        response = requests.post(self.__main_page_url__, data=data)
        soup = BeautifulSoup(response.content, 'html.parser')
        month_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectMes"}).findChildren()))
        zone_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectBarrio"}).findChildren()))[1:]
        return month_list, zone_list   

    def __get_data_values_from_table__(self, item:object):
        item_key = item.find('td', {"class" : "CabTab0"}).text.split('/')[1].strip()
        item_value = int(item.find('td', {"class" : "DatTab"}).text.replace('.', ''))
        return item_key, item_value

    def __get_density__(self, year:int, district:str, month:int, zones:list):
        data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':month,'selectDistrito':district, 'selectBarrio':zones,
                'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'}
        response = requests.post(self.__data_page_url__, data=data)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            table = soup.find_all('table')[1].findChildren('tr')[2:]
            return list(set(map(lambda x:self.__get_data_values_from_table__(x), table)))
        except:
            return []

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

        file_id = self.__api_client__.create_timeline('Density', date(year, 1,1),date(year, 12,31), 'Downloaded', file_path)
        complete_path_with_id= os.path.join(complete_path,f'{file_id}-{year}.csv')
        os.rename(file_path, complete_path_with_id)
        self.__logger__.info(f'file created {file_path} created')

    def download_density_file(self, years=[], months = []):
        self.__logger__.info(f'Downloading density files: Years: {",".join(years)}. Months: {",".join(months)}')
        district_list, year_list = self.__get_districts_and_years__()  
        if years != []:
            selected_year_list = list(set(year_list).intersection(set(years)))
        else:
            selected_year_list = year_list
        district_id_list = dict()
        neighborhood_id_list = dict()

        for year in selected_year_list:  
            final_list = []
            for district in district_list:
                month_list, zone_list = self.__get_available_months_and_zones__(year, district)   
                zone_list_set ={x[6:]:x[:5] for x in zone_list}
                if months != []:
                    selected_month_list = list(set(month_list).intersection(set(months)))
                else:
                    selected_month_list = month_list

                for month in selected_month_list:
                    self.__logger__.info(f'Retrieving data from {year} {month} {district}')
                    densities = self.__get_density__(year, district, month, zone_list)
                    for density in densities: 
                        month_number = int(month[0:2])                         
                        final_list.append({'year': year, 'month':month_number,'town_id':79,'districtId':int(district[:3]), 'district':district[3:], 'neighborhoodId':int(zone_list_set[density[0]]), 'neighborhood':density[0], 'value': density[1]}) 
            self.__write_csv_file__(final_list, year)
        self.__logger__.info(f'Density data downloaded')
        