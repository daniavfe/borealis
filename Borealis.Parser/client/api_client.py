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
        self.__timeline_endpoint__ :str = api_configuration.timeline_endpoint
        self.__town_endpoint__ :str = api_configuration.town_endpoint

    def get_existing_districts(self, page: int=1, per_page:int=20) -> list:
        response = requests.get(f'{ self.__base_url__}{self.__district_endpoint__}', params={'page':page, 'perPage':per_page})
        data = json.loads(response.content)
        return {item['id'] for item in data['items']}

    def get_existing_neighborhoods(self,  page: int=1, per_page:int=20) -> list:
        response = requests.get(f'{ self.__base_url__}{self.__neighborhood_endpoint__}', params={'page':page, 'perPage':per_page})
        data = json.loads(response.content)
        return {item['id'] for item in data['items']}

    def get_existing_towns(self, page:int=1, per_page:int=20) -> list:
        response = requests.get(f'{ self.__base_url__}{self.__town_endpoint__}', params={'page':page, 'perPage':per_page})
        data = json.loads(response.content)
        return {item['townId'] for item in data['items']}

    def create_district(self, id:int, town_id:int, name:str, surface:float) -> int:
        payload = {'id':id,'townId':town_id,'name': name, 'surface':surface}
        response = requests.post(f'{ self.__base_url__}{self.__district_endpoint__}', data=json.dumps(payload))
        return int(response.content)

    def create_neighborhood(self ,id:int, district_id:int, name:str, surface:float) -> int:
        payload = {'id':id,'districtId':district_id, 'name':name, 'surface':surface}
        response = requests.post(f'{ self.__base_url__}{self.__neighborhood_endpoint__}', data=json.dumps(payload))
        return int(response.content)

    def create_density(self, year:int, month:int, district_id:int, town_id:int, neighborhood_id:int, value:float) -> None:
        payload = {'townId':town_id, 'districtId':district_id, 'neighborhoodId':neighborhood_id, 'year':year, 'month':month, 'value':value}
        requests.post(f'{self.__base_url__}{self.__density_endpoint__}', data=json.dumps(payload))
   
    def create_densities(self, densities:list) -> list:
        response = requests.post(f'{self.__base_url__}{self.__density_endpoint__}/many', data=json.dumps(densities))
        items_not_created = json.loads(response.content)['itemsNotCreatedPositions']
        if len(items_not_created) > 0:
            return itemgetter(*items_not_created)(measurements)     
        return []

    def create_holiday(self, town_id:int, date:datetime, day_of_week:int, name:str, scope:str):
        payload = {"townId":town_id, "date":date, "dayOfWeek":day_of_week, "name":name, "scope":scope}
        requests.post(f'{self.__base_url__}{self.__holiday_endpoint__}', data=json.dumps(payload))

    def create_holidays(self, holidays:list) -> list:
        response = requests.post(f'{self.__base_url__}{self.__holiday_endpoint__}/many', data=json.dumps(holidays))
        items_not_created = json.loads(response.content)['itemsNotCreatedPositions']
        if len(items_not_created) > 0:
            return itemgetter(*items_not_created)(measurements)  
        return []

    def create_town(self, town_id:int, name:str):
        payload = {"townId":town_id, "name":name}
        requests.post(f'{self.__base_url__}{self.__town_endpoint__}', data=json.dumps(payload))

    def create_towns(self, towns:list) -> None:
        payload = list(map(lambda x: {"townId":x}, towns))
        requests.post(f'{self.__base_url__ }{self.__town_endpoint__}/many', data=json.dumps(payload))

    def create_stations(self, stations:list) -> None:
        payload = list(map(lambda x: {"id":x}, stations))
        requests.post(f'{self.__base_url__ }{self.__station_endpoint__}/many', data=json.dumps(payload))

    def create_magnitudes(self, magnitudes:list) -> None:
        payload = list(map(lambda x: {"id":x}, magnitudes))
        requests.post(f'{self.__base_url__}{self.__magnitude_endpoint__}/many', data=json.dumps(payload))

    def town_existence(self, towns:list) -> list:
        params = '?ids=' + '&ids='.join(towns)
        response = json.loads(requests.get(f'{self.__base_url__}{self.__town_endpoint__}/existence{params}').content)
        return response['ids'] 

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

    def create_measurement(self, datetime:datetime, magnitude_id:int, station_id:int, data:float, validation_code:str) -> None:
        payload = {"datetime": datetime.strftime("%Y-%m-%d %H:%M:%S"),"magnitudeId": magnitude_id, "stationId": station_id,"data": data, "validationCode": validation_code}
        requests.post(f'{self.__base_url__}{self.__measurement_endpoint__}',data=json.dumps(payload))

    def get_last_timeline(self, type:str) -> datetime:
        response = json.loads(requests.get(f'{self.__base_url__}{self.__timeline_endpoint__}/last', params={'type':type}).content)
        return response['lifeEnd']
    
    def create_timeline(self, type:str, life_start:datetime, life_end:datetime, status:str, details:str) -> int:
        payload = {'type':type, 'lifeStart':life_start.strftime('%Y-%m-%d %H:%M:%S'), 'lifeEnd':life_end.strftime('%Y-%m-%d %H:%M:%S'), 'status':status, 'details':details}
        response = requests.post(f'{self.__base_url__}{self.__timeline_endpoint__}', data=json.dumps(payload))
        return int(response.content)

    def update_timeline(self, timeline_id:int, status:str) -> None:
        payload = {'status':status}
        requests.put(f'{self.__base_url__}{self.__timeline_endpoint__}', params={'timelineId':timeline_id}, data=json.dumps(payload))