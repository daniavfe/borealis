from configuration import *
from density import DensityInitialLoad
from holiday import HolidayInitialLoad
from meteorology import MeteorologyInitialLoad
from common import EventHelper
from client import ApiClient
import json

# Configuración y dependencias
configuration:Configuration = Configuration.load_from_file('configuration.development.json')
api_client = ApiClient(configuration.api)

#density_initial_load = DensityInitialLoad(configuration.density, api_client)
#density_initial_load.load()

#holiday_initital_load = HolidayInitialLoad(configuration.holiday, api_client)
#holiday_initital_load.load()

#meteorology_initital_load = MeteorologyInitialLoad(configuration.meteorology, api_client)
#meteorology_initital_load.load()

pollution_initital_load = PollutionInitialLoad(configuration.pollution, api_client)
