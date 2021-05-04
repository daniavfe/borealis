from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from common import EventHelper
import requests
import csv
import json
import os

class DensityDownloader():
   
    def __init__(self, download_path):
        self.__main_page_url__ = 'http://www-2.munimadrid.es/TSE6/control/seleccionDatosBarrio'
        self.__density_data_url__ = 'http://www-2.munimadrid.es/TSE6/control/mostrarDatos'
        self.__download_path__ = download_path
        self.__event_helper__ = EventHelper()

    def __get_districts_and_years__(self):
        response = requests.get(self.__main_page_url__)
        soup = BeautifulSoup(response.content, 'html.parser')
        district_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectDistrito"}).findChildren()))[1:];
        year_list=list(map(lambda x:int(x['value'].strip()), soup.find(attrs={"name" : "selectAnio"}).findChildren()));
        return district_list, year_list;

    def __get_available_months_and_zones__(self, year, district):
        data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':'','selectDistrito':district,
                'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'};
        response = requests.post(self.__main_page_url__, data=data);
        soup = BeautifulSoup(response.content, 'html.parser');
        month_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectMes"}).findChildren()));
        zone_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectBarrio"}).findChildren()))[1:];
        return month_list, zone_list;   

    def __get_data_values_from_table__(self, item):
        item_key = item.find('td', {"class" : "CabTab0"}).text.split('/')[1].strip();
        item_value = int(item.find('td', {"class" : "DatTab"}).text.replace('.', ''));
        return item_key, item_value

    def __get_density__(self, year, district, month, zones):
        data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':month,'selectDistrito':district, 'selectBarrio':zones,
                'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'};
        response = requests.post( self.__density_data_url__, data=data);
        soup = BeautifulSoup(response.content, 'html.parser');
        try:
            table =  soup.find_all('table')[1].findChildren('tr')[2:];
            return list(set(map(lambda x:self.__get_data_values_from_table__(x), table)));
        except:
            return [];

    def __write_csv_file__(self, data, year):
        complete_path = os.path.join(self.__download_path__, str(year))
        if not os.path.isdir(complete_path):
            try:
                os.makedirs(complete_path)
            except:
                print(f"Error while creating directory: {path}")

        file_path = os.path.join(complete_path, f'{year}.csv')
        keys = data[0].keys();
        with open(file_path, 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        file_size = os.path.getsize(file_path)
        self.__event_helper__.file_download_event(file_path, file_size)
        print(f'file created {file_path} created');

    def download_density_file(self, years):
        district_list, year_list = self.__get_districts_and_years__()
        selected_year_list = list(set(year_list).intersection(set(years)))

        #año, mes, distrito, barrior, valor

        district_id_list = dict()
        neighborhood_id_list = dict()
        for year in selected_year_list:  
            final_list = []
            for district in district_list:
                print(f'Downloading district: {district}')
                month_list, zone_list = self.__get_available_months_and_zones__(year, district)      
                for month in month_list:
                    densities = self.__get_density__(year, district, month, zone_list);
                    for density in densities: 
                        #neighborhoodId = 0
                        #if(not density[0] in neighborhood_id_list):
                        #    neighborhoodId = insertNeighborhood(districtId, density[0])
                        #    neighborhood_id_list[density[0]] = neighborhoodId
                        #else:
                        #     neighborhoodId = neighborhood_id_list[density[0]]

                        month_number = int(month[0:2]);                         
                        final_list.append({'year': year, 'month':month_number, 'district':district[3:], 'zone':density[0], 'value': density[1]})        
            self.__write_csv_file__(final_list, year)

        print(f'Done')
        