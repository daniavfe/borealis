from client import ApiClient
from datetime import datetime, timedelta
from common import Logger
import requests
import csv
import json
import os

class DensityParser():

    def __init__(self, api_client:ApiClient, logger:Logger)->None:
        self.__api_client__:ApiClient = api_client
        self.__logger__ :Logger = logger

    def upload_file(self, path:str)->None:
        self.__logger__.info(f'Uploading {path} density file')
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            line_count = 0
            district_list = self.__api_client__.get_existing_districts(1, 1000)
            neighborhood_list =  self.__api_client__.get_existing_neighborhoods(1, 1000)
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1
                else:
                    year = row[0]
                    month = row[1]
                    district = row[2]
                    neighborhood = row[3]
                    value = row[4]

                    if not district in district_list :
                        self.__logger__.info(f'District {district} not found. Creating')
                        district_id = self.__api_client__.create_district(district, 0.0)
                        district_list[district] = district_id
                        self.__logger__.info(f'District {district} created with id {district_id}')
                    else:
                        district_id = district_list[district]

                    if not neighborhood in neighborhood_list:    
                        self.__logger__.info(f'Neighborhood {neighborhood} not found. Creating')
                        neighborhood_id =  self.__api_client__.create_neighborhood(district_id,neighborhood, 0.0)
                        neighborhood_list[neighborhood] = neighborhood_id
                        self.__logger__.info(f'Neighborhood {neighborhood} created with id {neighborhood_id}')
                    else:
                        neighborhood_id = neighborhood_list[neighborhood]

                    self.__api_client__.create_density(year, month, district_id, neighborhood_id, value)
                    line_count+= 1
            self.__logger__.info(f'File {path} upload completed')
                
    def upload_all_files(self, path:str)->None:
        if not os.path.isdir(path):
            self.__logger__.info(f'Path {path} is not correct')
            return             
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".csv"):
                    self.upload_file(os.path.join(root, file))

