from .density_configuration import DensityConfiguration
from .api_configuration import ApiConfiguration
from .holiday_configuration import HolidayConfiguration
from .meteorology_configuration import MeteorologyConfiguration
from .pollution_configuration import PollutionConfiguration
from .traffic_configuration import TrafficConfiguration

import json

class Configuration():
    def __init__(self, 
        api: ApiConfiguration, 
        density: DensityConfiguration, 
        holiday: HolidayConfiguration, 
        meteorology: MeteorologyConfiguration, 
        pollution: PollutionConfiguration, 
        traffic:TrafficConfiguration) -> None:

        self.api :ApiConfiguration = api
        self.density :DensityConfiguration = density
        self.holiday :HolidayConfiguration = holiday
        self.meteorology :MeteorologyConfiguration = meteorology
        self.pollution :PollutionConfiguration = pollution
        self.traffic :TrafficConfiguration = traffic

    def load_from_file(path:str):
        with open('configuration.development.json', 'r') as configuration_json:
            data = configuration_json.read()
            configuration :Configuration = Configuration(**json.loads(data)) 
            configuration.api :ApiConfiguration = ApiConfiguration(**configuration.api)
            configuration.density :DensityConfiguration = DensityConfiguration(**configuration.density)
            configuration.holiday :HolidayConfiguration = HolidayConfiguration(**configuration.holiday)
            configuration.meteorology = MeteorologyConfiguration(**configuration.meteorology)
            configuration.pollution = PollutionConfiguration(**configuration.pollution)
            configuration.traffic :TrafficConfiguration = TrafficConfiguration(**configuration.traffic)
            return configuration

