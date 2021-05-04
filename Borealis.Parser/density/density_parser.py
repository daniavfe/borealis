from datetime import datetime, timedelta
import requests
import csv
import json
import os

class DensityParser():

    def __init__(self):
        self.__api_url__ = 'http://127.0.0.1:5000/api/'
        self.__district_endpoint__ = 'density/district'
        self.__neighborhood_endpoint__ = 'density/neighborhood'
        self.__density_endpoint__ = 'density'

    def __get_existing_districts__(self):
        pfo_response = json.loads(requests.get(f'{self.__api_url__}{self.__district_endpoint__}?page=1&perPage=1000').content)
        return {item['name']:item['id'] for item in pfo_response['items']}

    def __get_existing_neighborhoods__(self):
        pfo_response = json.loads(requests.get(f'{self.__api_url__}{self.__neighborhood_endpoint__}?page=1&perPage=1000').content)
        return {item['name']:item['id'] for item in pfo_response['items']}

    def __insert_district__(self, name):
        payload = {"name": name, "surface":0.0}
        return int(requests.post(f'{self.__api_url__}{self.__district_endpoint__}', data=json.dumps(payload)).content)

    def __insert_neighborhood__(self, districtId, name):
        payload = {"districtId":districtId, "name":name, "surface":0.0}
        return int(requests.post(f'{self.__api_url__}{self.__neighborhood_endpoint__}', data=json.dumps(payload)).content)

    def __insert_density__(self, year, month, districtId, neighborhoodId, value):
        payload = {"districtId":districtId, "neighborhoodId":neighborhoodId, "year":year, "month":month, "value":value}
        requests.post(f'{self.__api_url__}{self.__density_endpoint__}', data=json.dumps(payload))
        return

    def __load_file__(self, path):
        with open(path) as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            line_count = 0
            district_list = self.__get_existing_districts__()
            neighborhood_list =  self.__get_existing_neighborhoods__()
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
                        district_id = self.__insert_district__(district)
                        district_list[district] = district_id
                    else:
                        district_id = district_list[district]

                    if not neighborhood in neighborhood_list:
                        neighborhood_id = self.__insert_neighborhood__(district_id, neighborhood)
                        neighborhood_list[neighborhood] = neighborhood_id
                    else:
                        neighborhood_id = neighborhood_list[neighborhood]

                    self.__insert_density__(year, month, district_id, neighborhood_id, value)
                    line_count+= 1

