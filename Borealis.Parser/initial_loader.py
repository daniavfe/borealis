from configuration import *
from density import DensityInitialLoader
from holiday import HolidayInitialLoader
from meteorology import MeteorologyInitialLoader
from pollution import PollutionInitialLoader
from common import Logger
from client import ApiClient
import json

# Configuración y dependencias
configuration :Configuration = Configuration.load_from_file('configuration.development.json')

#Cliente de la API
api_client :ApiClient = ApiClient(configuration.api)

#Logger
logger :Logger = Logger()

#Carga inicial de densidades
#density_initial_loader :DensityInitialLoader= DensityInitialLoader(configuration.density, api_client, logger)
#density_initial_loader.load()

#Carga inicial de vacaciones
holiday_initital_loader :HolidayInitialLoader= HolidayInitialLoader(configuration.holiday, api_client, logger)
holiday_initital_loader.load()

#Carga inicial de datos meteorológicos
#meteorology_initital_loader:MeteorologyInitialLoader = MeteorologyInitialLoader(configuration.meteorology, api_client, logger)
#meteorology_initital_loader.load()

#Carga inicial de calidad del aire
#pollution_initital_loader = PollutionInitialLoader(configuration.pollution, api_client, logger)
#pollution_initital_loader.load()