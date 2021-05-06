from configuration import ApiConfiguration
from datetime import datetime, timedelta
from operator import itemgetter 
import requests
import json

class ApiClient():
    def __init__(self, api_configuration: ApiConfiguration) -> None:
        self.__base_url__ :str = api_configuration.base_url
        self.__district_endpoint__ :str = api_configuration.district_endpoint
        self.__neighborhood_endpoint__ :str = api_configuration.neighborhood_endpoint
        self.__density_endpoint__ :str = api_configuration.density_endpoint
        self.__holiday_endpoint__ :str = api_configuration.holiday_endpoint
        self.__measurement_endpoint__ :str = api_configuration.measurement_endpoint
        self.__station_endpoint__ :str = api_configuration.station_endpoint
        self.__magnitude_endpoint__ :str = api_configuration.magnitude_endpoint
        self.__event_endpoint__ :str = api_configuration.event_endpoint

    def get_existing_districts(self, page: int=1, per_page:int=20) -> list:
        response = requests.get(f'{ self.__base_url__}{self.__district_endpoint__}', params={'page':page, 'perPage':per_page})
        data = json.loads(response.content)
        return {item['name']:item['id'] for item in data['items']}

    def get_existing_neighborhoods(self,  page: int=1, per_page:int=20) -> list:
        response = requests.get(f'{ self.__base_url__}{self.__neighborhood_endpoint__}', params={'page':page, 'perPage':per_page})
        data = json.loads(response.content)
        return {item['name']:item['id'] for item in data['items']}

    def create_district(self, name:str, surface:float) -> int:
        payload = {'name': name, 'surface':surface}
        response = requests.post(f'{ self.__base_url__}{self.__district_endpoint__}', data=json.dumps(payload))
        return int(response.content)

    def create_neighborhood(self, district_id:int, name:str, surface:float) -> int:
        payload = {'districtId':district_id, 'name':name, 'surface':surface}
        response = requests.post(f'{ self.__base_url__}{self.__neighborhood_endpoint__}', data=json.dumps(payload))
        return int(response.content)

    def create_density(self, year:int, month:int, district_id:int, neighborhood_id:int, value:float) -> None:
        payload = {'districtId':district_id, 'neighborhoodId':neighborhood_id, 'year':year, 'month':month, 'value':value}
        requests.post(f'{self.__base_url__}{self.__density_endpoint__}', data=json.dumps(payload))
   
    def create_holiday(self, date:datetime, day_of_week:int, name:str, scope:str):
        payload = {"date":date, "dayOfWeek":day_of_week, "name":name, "scope":scope}
        requests.post(f'{self.__base_url__}{self.__holiday_endpoint__}', data=json.dumps(payload))

    def create_stations(self, stations:list) -> None:
        payload = list(map(lambda x: {"id":x}, stations))
        requests.post(f'{self.__base_url__ }{self.__station_endpoint__}/many', data=json.dumps(payload))

    def create_magnitudes(self, magnitudes:list) -> None:
        payload = list(map(lambda x: {"id":x}, magnitudes))
        requests.post(f'{self.__base_url__}{self.__magnitude_endpoint__}/many', data=json.dumps(payload))

    def station_existence(self, stations:list) -> list:
        params = '?ids=' + '&ids='.join(stations)
        response = json.loads(requests.get(f'{self.__base_url__}{self.__station_endpoint__}/existence{params}').content)
        return response['ids'] 

    def magnitude_existence(self, magnitudes:list) -> list:
        params = '?ids=' + '&ids='.join(magnitudes)
        response = json.loads(requests.get(f'{self.__base_url__}{self.__magnitude_endpoint__}/existence{params}').content)
        return response['ids'] 

    def create_measurements(self, measurements:list) -> list:
        response = requests.post(f'{self.__base_url__}{self.__measurement_endpoint__}/many', data=json.dumps(measurements))
        items_not_created = json.loads(response.content)['itemsNotCreatedPositions']
        if len(items_not_created) > 0:
            return itemgetter(*items_not_created)(measurements)     
        return []

    def create_measurement(self, datetime:datetime, magnitude_id:int, station_id:int, data:float, validation_code:str)->None:
        payload = {"datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id,"data": data, "validationCode": validation_code}
        requests.post(f'{self.__base_url__}{self.__measurement_endpoint__}',data=json.dumps(payload))